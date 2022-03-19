import sys
from datetime import datetime
import time
from selenium.webdriver.common.by import By
import requests as requests
from requests_html import HTMLSession
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
# import config
# from parser_vse_pesni import open_input_file, get_soup, record_to_csv, send_telegram, stop_list, time_intrvals
from selenium.webdriver.support.wait import WebDriverWait

'''
 Парсер заданий на kwork.ru
'''

if __name__ == '__main__':
    print('Стартуем!!!')

    login_url = 'https://kwork.ru/'
    base_url = 'https://kwork.ru/projects'
    options = uc.ChromeOptions()
    options.user_data_dir = '/home/qqq/.config/google-chrome/Default'
    driver = uc.Chrome(options=options)
    driver.get(login_url)
    time.sleep(8)
    try:
        login_js = driver.find_element(by=By.XPATH, value='//*[@id="body"]/div[4]/div[2]/div[1]/div/div[2]/div[4]/ul/li[1]/a').click()
        time.sleep(1)
    except:
        print('tiri piri')
    else:
        username = driver.find_element(by=By.XPATH, value='//*[@id="form-login"]/div[1]/div[3]/div[2]/input')
        username.send_keys('aswd25@yandex.ru')
        password = driver.find_element(by=By.XPATH, value='//*[@id="form-login"]/div[1]/div[3]/div[3]/div[1]/input')
        password.send_keys('a1234567')
        login_button = driver.find_element(by=By.XPATH, value='//*[@id="form-login"]/div[1]/div[3]/button[1]').click()
        time.sleep(5)
    driver.get(base_url)
    html_1 = driver.page_source
    with open('1.html', 'w') as f:
        f.write(html_1)
    time.sleep(5)

        # while True:
        #     print(datetime.now())
        #     soup = get_soup(url)
        #     title = soup.find_all('div', config.title_teg)
        #     for i in title:
        #         title = i.find_next('div')
        #         if stop_list(title):
        #             continue
        #         projects_from_csv = open_input_file('output.csv')
        #         if title.text in projects_from_csv:
        #             print(title.text, 'УЖЕ ЕСТЬ!!!!')
        #             continue
        #         description = i.find_next('div', class_='breakwords first-letter js-want-block-toggle js-want-block-toggle-full hidden')
        #         text = []
        #         text.append(title.text)
        #         text.append(description.text)
        #         text.append(title.a["href"])
        #         tg_text = title.text+'\n'+description.text+'\n'+title.a["href"]
        #         send_telegram(tg_text)
        #         record_to_csv(text)
        #         time.sleep(2)
        #
        #     time_intrvals(config.time_interval)
        #     print('='*77)
        #     print(datetime.now())
        #     print('Проверяю...')
        #     print('=' * 77)