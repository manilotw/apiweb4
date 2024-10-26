import datetime
import requests
from general_functions import download_picture
from environs import Env


env = Env()
env.read_env()

def fetch_epic_images(count, nasa_api):
    url = env.str('API_NASA_EPIC')
    
    for number in range(0, count):
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        
        date = json_data[number]['date'].split(' ')[0]
        title = json_data[number]['image']
        datetimedate = datetime.date.fromisoformat(date)
        date = datetimedate.strftime('%Y/%m/%d')
        url_image = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{title}.png?api_key={nasa_api}'
        filename = f'images/nasa_epic_{number}.png'
        
        download_picture(filename, url_image)

def main():
    nasa_token = env.str('NASA_TOKEN')
    fetch_epic_images(5, nasa_token)

if __name__ == '__main__':
    main()
