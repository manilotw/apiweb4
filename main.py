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

def fetch_spacex_last_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    json_data = response.json()
    photo_links = json_data['links']['flickr']['original']
    for photo_number, link in enumerate(photo_links):
        response = requests.get(link)
        response.raise_for_status()
        filename = f'images/spacex_{photo_number}.jpeg'
        with open(filename, 'wb') as file:
            file.write(response.content)

def get_file_extension(url):
    scheme, netloc, path, query, fragment = urllib.parse.urlsplit(url)
    path = urllib.parse.unquote(path)
    fragment, format = os.path.splitext(path)
    return format

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
        fragment, format = os.path.splitext(photo_url)
        response = requests.get(photo_url)
        response.raise_for_status()
        filename = f'images/nasa_apod_{number-1}{format}'
        
        with open(filename, 'wb') as file:
            file.write(response.content)
      
def fetch_epic_images(url,count, nasa_api):
    for number in range(0, count):
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        
        date = json_data[number]['date'].split(' ')[0]
        title = json_data[number]['image']
        datetimedate = datetime.date.fromisoformat(date)
        date = datetimedate.strftime('%Y/%m/%d')
        url_image = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{title}.png?api_key={nasa_api}'
        response = requests.get(url_image)
        response.raise_for_status()
        filename = f'images/nasa_epic_{number}.png'
        
        with open(filename, 'wb') as file:
            file.write(response.content)
    
def main():
    env=Env()
    env.read_env()
    filename = 'images/hubble.jpeg'
    url = 'https://api.spacexdata.com/v4/launches/5eb87d47ffd86e000604b38a'
    NASA_TOKEN = env.str('NASA_TOKEN')
    url_ex = 'https://example.com/txt/hello%20world.txt?v=9#python'
    api_nasa_apod = 'https://api.nasa.gov/planetary/apod'
    api_nasa_epic = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY'

if __name__ == '__main__':
    main()

        






