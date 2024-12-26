from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    import asyncio
    from datetime import datetime, timedelta
    from app.hubspot_sync import HubSpotSync
    from app.config import APP_CONFIG, MESSAGE_TEMPLATES

    class ArveaBot:
        def __init__(self, token: str):
            self.updater = Updater(token, use_context=True)
            self.dp = self.updater.dispatcher
            self.hubspot = HubSpotSync(APP_CONFIG['HUBSPOT_API_KEY'])
            self.setup_handlers()
        
        def setup_handlers(self):
            self.dp.add_handler(CommandHandler("start", self.start))
            self.dp.add_handler(CallbackQueryHandler(self.handle_button))
            self.dp.add_handler(MessageHandler(Filters.text, self.handle_message))
        
        def create_landing_page(self, distributor_id: str) -> str:
            try:
                distributor = self.hubspot.get_contact(distributor_id)
                if distributor:
                    message = f"""
                    🌟 Welcome to Arvea Elite! 
                    Join {distributor['properties']['firstname']} {distributor['properties']['lastname']}'s Successful Team

                    🎯 What We Offer:
                    • Financial Freedom
                    • Flexible Schedule
                    • Professional Training
                    • Global Community

                    Choose Your Path:
                    """
                    
                    buttons = [
                        [InlineKeyboardButton("Join Opportunity", url=distributor['properties']['opportunity_link'])],
                        [InlineKeyboardButton("Shop Products", url=distributor['properties']['shop_link'])],
                        [InlineKeyboardButton("Learn More", callback_data=f"info_{distributor_id}")]
                    ]
                    
                    return message, InlineKeyboardMarkup(buttons)
                else:
                    return "Distributor not found.", None
            except Exception as e:
                return f"Error fetching distributor: {e}", None
        
        def start_autoresponder(self, lead_id: str):
            """Starts the autoresponder sequence for a lead using Telegram bot."""
            try:
                lead = self.hubspot.get_contact(lead_id)
                if lead:
                    chat_id = lead['properties']['email']  # Assuming email is used as chat_id for simplicity
                    sequence = MESSAGE_TEMPLATES['training_sequence']
                    
                    for message_data in sequence:
                        delay_days = message_data['day']
                        message_content = message_data['content']
                        send_time = datetime.now() + timedelta(days=delay_days)
                        self.schedule_message(chat_id, message_content, send_time)
                else:
                    print(f"Lead not found in HubSpot: {lead_id}")
            except Exception as e:
                print(f"Error starting autoresponder: {e}")
        
        def schedule_message(self, chat_id: str, message: str, send_time: datetime):
            """Schedules a message to be sent via the Telegram bot."""
            delay = (send_time - datetime.now()).total_seconds()
            asyncio.get_event_loop().call_later(delay, self.send_message, chat_id, message)
        
        def send_message(self, chat_id: str, message: str):
            """Sends a message via the Telegram bot."""
            self.updater.bot.send_message(chat_id=chat_id, text=message)
        
        def start(self, update, context):
            distributor_id = "201"  # Example distributor ID
            message, reply_markup = self.create_landing_page(distributor_id)
            if reply_markup:
                update.message.reply_text(message, reply_markup=reply_markup)
            else:
                update.message.reply_text(message)
        
        def handle_button(self, update, context):
            query = update.callback_query
            query.answer()
            if query.data.startswith("info_"):
                distributor_id = query.data.split("_")[1]
                query.edit_message_text(text=f"Info for distributor {distributor_id}")
        
        def handle_message(self, update, context):
            update.message.reply_text(f"You said: {update.message.text}")
