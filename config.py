import os

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")
    HUBSPOT_ACCESS_TOKEN = os.getenv("HUBSPOT_ACCESS_TOKEN", "YOUR_HUBSPOT_ACCESS_TOKEN")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")