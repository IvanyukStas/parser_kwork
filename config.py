import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
channel_id = os.getenv('channel_id')
title_teg = os.getenv('title_teg') or 'wants-card__left'

#если слова есть в заголовке, то не парсить
break_word = ['1с', 'верстка', 'android', 'ios', 'yii', 'php', 'java', 'bitrix 1c',
              'bitrix', 'wp', 'Битрикс', 'Word press', 'Wordpress', 'Laravel']

#время через которое бот заходит на сайт и парсит инфу
time_interval = 1200


