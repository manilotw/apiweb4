import telegram
from environs import Env


env = Env()
env.read_env()
token = env.str('TG_BOT_TOKEN')
bot = telegram.Bot(token=token)
chat_id = '@doubletesttg'
document = open('images/spacex_1.jpeg', 'rb')
bot.send_document(chat_id=chat_id, document=document)