import time
import config
from parser_vse_pesni import open_input_file, get_soup, record_to_csv, send_telegram

'''
 Парсер заданий на kwork.ru
'''

if __name__ == '__main__':

    while True:
        time.sleep(300)
        url = 'https://kwork.ru/projects?c=11'
        soup = get_soup(url)
        title = soup.find_all('div', config.title_teg)
        for i in title:
            title = i.find_next('div')
            projects_from_csv = open_input_file('output.csv')
            if title.text in projects_from_csv:
                print(title.text, 'УЖЕ ЕСТЬ!!!!')
                break
            description = i.find_next('div', class_='breakwords first-letter js-want-block-toggle js-want-block-toggle-full hidden')
            text = []
            text.append(title.text)
            text.append(description.text)
            text.append(title.a["href"])
            tg_text = title.text+'\n'+description.text+'\n'+title.a["href"]
            send_telegram(tg_text)
            record_to_csv(text)
            time.sleep(2)