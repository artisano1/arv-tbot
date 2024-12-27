from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from config import Config

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Join Opportunity", url="YOUR_OPPORTUNITY_LINK")],
        [InlineKeyboardButton("Shop", url="YOUR_SHOP_LINK")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome to Arvea Elite! Choose an option:", reply_markup=reply_markup)

def start_bot():
    updater = Updater(Config.TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()