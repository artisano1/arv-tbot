import streamlit as st
    from app.pages.landing import show_landing_page
    from app.pages.admin.dashboard import show_admin_dashboard
    from app.pages.distributor.dashboard import show_distributor_dashboard
    from app.bot_handler import ArveaBot
    from app.config import APP_CONFIG

    # Initialize bot
    bot = ArveaBot(APP_CONFIG['TELEGRAM_BOT_TOKEN'])
    bot.updater.start_polling()

    def main():
        # Check if user is logged in
        if 'user_id' not in st.session_state:
            show_landing_page()
            return
        
        # Route to appropriate dashboard based on role
        if st.session_state.get('role') == 'admin':
            show_admin_dashboard()
        else:
            show_distributor_dashboard()

    if __name__ == "__main__":
        main()
