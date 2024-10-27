import requests
import urllib.parse
import os
from general_functions import download_picture, get_file_extension
from environs import Env


env = Env()
env.read_env()

def fetch_apod_images(image_count, nasa_api):
    nasa_apod_url = env.str('API_NASA_APOD')

    params = {
        'api_key': nasa_api,
        'count': image_count
    }

    response = requests.get(nasa_apod_url, params=params)
    response.raise_for_status()
    images_data = response.json()

    for index, image_info in enumerate(images_data):
        image_url = image_info['url']
        image_url = urllib.parse.unquote(image_url)
        _, filename = os.path.split(image_url)
        file_extension = get_file_extension(image_url)
        full_filename = f'images/nasa_apod_{index}{file_extension}'
        
        download_picture(full_filename, image_url)

def main():
    nasa_api_key = env.str('NASA_TOKEN')

    fetch_apod_images(30, nasa_api_key)

if __name__ == '__main__':
    main()
