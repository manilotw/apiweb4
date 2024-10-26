import requests
import argparse
from general_functions import download_picture


def fetch_spacex_last_launch(launch_id=None):
    if launch_id:
        url = f'https://api.spacexdata.com/v4/launches/{launch_id}'
    else:
        url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    spacex_images_data = response.json()
    photo_links = spacex_images_data['links']['flickr']['original']
    for photo_number, link in enumerate(photo_links):
        filename = f'images/spacex_{photo_number}.jpeg'
        download_picture(filename, link)

def main():
    parser = argparse.ArgumentParser(description='Скачать фото запуска SpaceX')
    parser.add_argument('--launch_id', help='ID запуска SpaceX')
    args = parser.parse_args()

    launch_id = args.launch_id

    fetch_spacex_last_launch(launch_id)

if __name__ == '__main__':
    main()
