import telegram
from environs import Env
import time
import random
import os
import argparse


def main():
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env.str('TG_BOT_TOKEN'))
    chat_id = '@doubletesttg'
    images_path = 'images'

    parser = argparse.ArgumentParser(description='Скрипт для публикаций всех фотографий')
    parser.add_argument('--PUBLICATION_INTERVAL', type=int, help='Интервал для публикаций(в сек.)')
    args = parser.parse_args()
    publocation_interval = args.PUBLICATION_INTERVAL
    all_files = []

    if publocation_interval==None:
        publocation_interval = env.int('PUBLICATION_INTERVAL')

    for dirpath, dirnames, filenames in os.walk(images_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            all_files.append(file_path)

    while True:
        random.shuffle(all_files)
        for file in all_files:
            with open(file, 'rb') as image:
                bot.send_document(chat_id=chat_id, document=image)
            time.sleep(publocation_interval)

if __name__ == '__main__':
    main()