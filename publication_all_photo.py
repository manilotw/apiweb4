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
    chat_id = env.str('TG_CHAT_ID')  
    images_path = 'images'

    parser = argparse.ArgumentParser(description='Скрипт для публикаций всех фотографий')
    parser.add_argument('--PUBLICATION_INTERVAL', type=int, default=14400, help='Интервал для публикаций (в секундах, по умолчанию 14400 сек.)')
    args = parser.parse_args()
    publication_interval = args.PUBLICATION_INTERVAL

    all_files = []
    for dirpath, dirnames, filenames in os.walk(images_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            all_files.append(file_path)

    while True:
        random.shuffle(all_files)
        for file in all_files:
            with open(file, 'rb') as image:
                bot.send_document(chat_id=chat_id, document=image)
            time.sleep(publication_interval)

if __name__ == '__main__':
    main()
