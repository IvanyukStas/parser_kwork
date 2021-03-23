import csv
import requests
from bs4 import BeautifulSoup
import locale
import config


def open_input_file()->list:
    url = []
    with open('input.csv', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            url.append(row[0])
    return url


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def find_artist(soup)-> str:
    category = soup.find_all('span', itemprop=config.artist_teg)
    category = category[2].text
    return category

def find_song_name(soup)->str:
    title = soup.find_all('span', class_=config.song_name_teg)
    title = title[0].text
    return title

def find_song_text(soup)->str:
    text_song = soup.find_all('div', class_="song_text left_pos")
    text_song = text_song[0].text.lstrip('\n')
    text_song = text_song.replace('\r', '')
    return text_song


def record_to_csv(data):
    locale.setlocale(locale.LC_ALL, '')
    DELIMITER = ';' if locale.localeconv()['decimal_point'] == ',' else ','
    with open('output.csv', 'a', encoding='utf-8', newline='') as file_w:
        writer = csv.writer(file_w, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        writer.writerows([data])
    print('RECORD COMLETE!')