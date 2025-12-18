from telegram import Bot
from config.settings import TELEGRAM_TOKEN, CHANNEL_ID

def post_to_telegram(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=CHANNEL_ID, text=message)
