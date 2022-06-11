import os
from dotenv import load_dotenv


load_dotenv()


class ConfigGeneral:
    TOKEN = os.getenv("TOKEN")
    CHANNEL_ID = os.getenv("channel_id")
    # время через которое бот заходит на сайт и парсит инфу
    TIME_INTERVAL = 1200


class ConfigKwork:
    TITLE_TAG = os.getenv("title_teg") or "wants-card__left"


class ConfigFilter:
    # если слова есть в заголовке, то не парсить
    BREAK_WORD = [
        "1с",
        "верстка",
        "android",
        "ios",
        "yii",
        "php",
        "java",
        "bitrix 1c",
        "bitrix",
        "wp",
        "Битрикс",
        "Word press",
        "Wordpress",
        "Laravel",
    ]
