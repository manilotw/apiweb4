import urllib.parse
import requests
import os
import datetime
from environs import Env


def download_picture(filename, url):
    response = requests.get(url)
    response.raise_for_status()

    with open (filename, 'wb') as file:
        file.write(response.content)

def get_file_extension(url):
    scheme, netloc, path, query, fragment = urllib.parse.urlsplit(url)
    path = urllib.parse.unquote(path)
    fragment, format = os.path.splitext(path)
    return format

def main():
    env=Env()
    env.read_env()
    filename = 'images/hubble.jpeg'
    url_spacex_images = 'https://api.spacexdata.com/v4/launches/5eb87d47ffd86e000604b38a'
    NASA_TOKEN = env.str('NASA_TOKEN')
    url_ex = 'https://example.com/txt/hello%20world.txt?v=9#python'
    api_nasa_apod = 'https://api.nasa.gov/planetary/apod'
    api_nasa_epic = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY'

if __name__ == '__main__':
    main()

        






