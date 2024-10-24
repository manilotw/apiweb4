import datetime
import requests
from general_functions import download_picture


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
        filename = f'images/nasa_epic_{number}.png'
        
        download_picture(filename, url_image)