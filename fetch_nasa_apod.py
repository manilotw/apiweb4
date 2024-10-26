import requests
import urllib.parse
import os
from general_functions import download_picture, get_file_extension
from environs import Env


env = Env()
env.read_env()

def fetch_apod_images(count, nasa_api):
    url = env.str('API_NASA_APOD')

    for number in range(1, count+1):

        params = {
            'api_key': nasa_api,
            'count': number
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        json_data = response.json()
        photo_url = json_data[0]['url']
        photo_url = urllib.parse.unquote(photo_url)
        fragment, filename = os.path.split(photo_url)
        format = get_file_extension(photo_url)
        filename = f'images/nasa_apod_{number-1}{format}'
        
        download_picture(filename, photo_url)

def main():
    nasa_api = env.str('NASA_TOKEN')

    fetch_apod_images(30, nasa_api)

if __name__ == '__main__':
    main()
