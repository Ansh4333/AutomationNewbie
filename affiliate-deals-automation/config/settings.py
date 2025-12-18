import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
AFFILIATE_TAG = os.getenv("AFFILIATE_TAG")
DB_PATH = "deals.db"
