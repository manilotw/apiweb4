import telegram
from environs import Env


env = Env()
env.read_env()
token = env.str('TG_BOT_TOKEN')
bot = telegram.Bot(token=token)
chat_id = '@doubletesttg'

bot.send_message(chat_id=chat_id, text='Hello')