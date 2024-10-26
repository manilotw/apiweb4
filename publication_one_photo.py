import telegram
from environs import Env
import random
import os
import argparse

env = Env()
env.read_env()

bot = telegram.Bot(token=env.str('TG_BOT_TOKEN'))
chat_id = '@doubletesttg'
images_path = 'images'

parser = argparse.ArgumentParser()
parser.add_argument('--file_number', type=int, help='Какую фотографию опубликовать?')
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

    
        

