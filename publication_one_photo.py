import telegram
from environs import Env
import random
import os
import argparse


def main():
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env.str('TG_BOT_TOKEN'))
    chat_id = env.str('TG_CHAT_ID')
    images_path = 'images'

    parser = argparse.ArgumentParser(description="Скрипт для публикации фотографий")
    parser.add_argument('--file_number', type=int, help='Номер файла для отправки. Если не указан, отправляется случайный файл')
    args = parser.parse_args()
    file_number = args.file_number
    all_files = []

    for dirpath, dirnames, filenames in os.walk(images_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            all_files.append(file_path)

    if file_number:
        file = all_files[file_number - 1]
    else:
        file = random.choice(all_files)

    with open(file, 'rb') as image:
        bot.send_document(chat_id=chat_id, document=image)

if __name__ == '__main__':
    main()

    
        

