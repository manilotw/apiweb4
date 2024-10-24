import requests
import urllib.parse
import os
from general_functions import download_picture, get_file_extension


def fetch_apod_images(url, count, nasa_api):
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