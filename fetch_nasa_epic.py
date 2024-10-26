import datetime
import requests
from general_functions import download_picture
from environs import Env

def fetch_epic_images(api_url, count, api_key):
    response = requests.get(api_url)
    response.raise_for_status()
    epic_images_data = response.json()
    
    for number in range(count):
        date_str = epic_images_data[number]['date'].split(' ')[0]
        title = epic_images_data[number]['image']
        formatted_date = datetime.date.fromisoformat(date_str).strftime('%Y/%m/%d')
        
        url_image_base = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{title}.png'
        params = {'api_key': api_key}
        
        download_picture(f'images/nasa_epic_{number}.png', url_image_base, params=params)

def main():
    env = Env()
    env.read_env()

    nasa_token = env.str('NASA_TOKEN')
    nasa_epic_url = env.str('API_NASA_EPIC')

    fetch_epic_images(nasa_epic_url, 5, nasa_token)

if __name__ == '__main__':
    main()
