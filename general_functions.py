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

    api_nasa_apod = ''


        






