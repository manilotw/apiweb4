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

### Как работает `publication_one_photo`

Для того что бы отправить случайное изоюражение просто запустите скрипт командой:
```
python publication_one_photo.py 
```

А если вы хотите отправить конкретное изображение, то укажите его номер таким образом:
```
python publication_one_photo.py --file_number 2
```

### Как работает `publication_all_photo`

Для отправки всех изображение интервалом в 4 часа (по умолчанию), нужно запустить скрипт командой:
```
python publication_all_photo.py
```
А если самому хочется задать интервал нужно запустить скрипт и указать интервал в секундах, например 3600 (1 час):
```
python publication_all_photo.py --publication_interval 3600
```
Важно отметить что программа будет работать бесконечно после запуска скрипта, и в случае публикаций последней фотографий с папки, публикация пойдет по кругу в случайном порядке!

Для остановки скрипта нужно зажать клавиши `Ctrl + C`

### Переменные окружения

- NASA_TOKEN - Токен с сайта NASA API

- TG_BOT_TOKEN - Токен бота телеграм

- API_NASA_EPIC - Ссылка для получения JSON фотографий NASA EPIC

- API_NASA_APOD - Ссылка на API NASA APOD

- PUBLICATION_INTERVAL - Интервал публикаций в секундах

- TG_CHAT_ID - ID телеграм-канала начиная с `@` (например: `@channelid`)
