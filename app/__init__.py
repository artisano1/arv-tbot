from flask import Flask
from .routes import main
from .bot.telegram_bot import start_bot

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    app.register_blueprint(main)
    start_bot()  # Start the Telegram bot
    return app