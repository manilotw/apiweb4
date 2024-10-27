import urllib.parse
import requests
import os


def download_picture(filename, url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open (filename, 'wb') as file:
        file.write(response.content)

def get_file_extension(url):
    scheme, netloc, path, query, fragment = urllib.parse.urlsplit(url)
    path = urllib.parse.unquote(path)
    fragment, format = os.path.splitext(path)
    return format


        






