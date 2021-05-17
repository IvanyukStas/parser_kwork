import csv
import os
import sys
import time

import requests
from bs4 import BeautifulSoup
import config


def open_input_file(input_file) -> list:
    url = []
    if not os.path.exists('output.csv'):
       f = open('output.csv', 'w')
       f.close()
    with open(input_file) as file:
        reader = csv.reader(file, delimiter=';',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            url.append(row[0])
    return url


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def record_to_csv(data):
    with open('output.csv', 'a', encoding='utf-8', newline='') as file_w:
        writer = csv.writer(file_w, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        writer.writerows([data])
    print('RECORD COMLETE!')


def send_telegram(text: str):
    TOKEN = config.TOKEN
    url = "https://api.telegram.org/bot"
    channel_id = config.channel_id
    url += TOKEN
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        raise Exception("post_text error")

def stop_list(title):
    if config.break_word == []:
        return None
    for stop_word in config.break_word:
        if stop_word.lower() in title.text.lower():
            print('Титле в стоп листе!!!!')
            print(stop_word, "============= Стоп ворд")
            print(title.text, '============= Запрещенный титле')
            return True

def time_intrvals(n):
    write, flush = sys.stdout.write, sys.stdout.flush
    for i in reversed(range(n)):
        write(str(i))
        flush()
        write('\x08' * 10)
        time.sleep(0.5)