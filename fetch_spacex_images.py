import requests
import argparse
from general_functions import download_picture


def fetch_spacex_last_launch(launch_id='latest'):
    url = f'https://api.spacexdata.com/v4/launches/{launch_id}'
    
    response = requests.get(url)
    response.raise_for_status()
    spacex_images = response.json()
    photo_links = spacex_images['links']['flickr']['original']
    
    for photo_number, link in enumerate(photo_links):
        filename = f'images/spacex_{photo_number}.jpeg'
        download_picture(filename, link)


def main():
    parser = argparse.ArgumentParser(description='Скачать фото запуска SpaceX')
    parser.add_argument('--launch_id', default='latest', help='ID запуска SpaceX (по умолчанию последний запуск)')
    args = parser.parse_args()

    launch_id = args.launch_id

    fetch_spacex_last_launch(launch_id)


if __name__ == '__main__':
    main()
