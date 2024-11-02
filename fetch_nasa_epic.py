import datetime
import requests
from general_functions import download_picture
from environs import Env


def fetch_epic_images(count, api_key):
    
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY'
    response = requests.get(nasa_epic_url)
    response.raise_for_status()
    epic_images = response.json()
    
    for number in range(count):
        date_str = epic_images[number]['date'].split(' ')[0]
        title = epic_images[number]['image']
        formatted_date = datetime.date.fromisoformat(date_str).strftime('%Y/%m/%d')
        
        base_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{title}.png'
        params = {'api_key': api_key}
        
        download_picture(f'images/nasa_epic_{number}.png', base_image_url, params=params)

def main():
    env = Env()
    env.read_env()

    nasa_token = env.str('NASA_TOKEN')
    image_count = 5

    fetch_epic_images(image_count, nasa_token)

if __name__ == '__main__':
    main()
