# Космический Телеграм

Проект написан для публикаций и скачивания космических фотографий из сайтов NASA и SpaceX

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Описание скриптов

- `fetch_nasa_apod` - скачивает космическое фото дня (кол-во 30 шт)

- `fetch_nasa_epic` - скачивает фотографий планеты Земля (кол-во 5 шт)

- `fetch_spacex_images` - скачивает фотографий запусков ракет SpaceX

- `general_functions` - находятся функций которые используются в скриптах

- `publication_all_photo` - публикует фотографий с интервалом, а когда они закончатся то заново публикует но случайном порядке

- `publication_photo` - публикует указанную фотографию, а если она не указана публикует случайную фотографию

### Как работает `publication_photo`

Необходимо запустить скрипт и указать номер фотографий (например 3)

```
python publication_photo.py --file_number 3
```
В ином же случае скрипт опубликует случаную фотографию

### Как работает `publication_all_photo`

необходимо запустить скрипт и указать интервал публикаций в секундах (например 3600)

```
python publicatiom_all_photo.py --PUBLICATION_INTERVAL 3600
```
Если не указать интервал он будет по умолчанию 4 часа (14400 секунд)

### Переменные окружения

- NASA_TOKEN - Токен с сайта NASA API

- TG_BOT_TOKEN - Токен бота телеграм

- API_NASA_EPIC - Ссылка для получения JSON фотографий NASA EPIC

- API_NASA_APOD - Ссылка на API NASA APOD

- PUBLICATION_INTERVAL - Интервал публикаций в секундах

- TG_CHAT_ID - ID телеграм-канала начиная с `@` (например: `@channelid`)
