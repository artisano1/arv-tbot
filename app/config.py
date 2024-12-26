import os
    from dotenv import load_dotenv

    load_dotenv()

    # App configuration
    APP_CONFIG = {
        'SECRET_KEY': os.getenv('SECRET_KEY'),
        'TELEGRAM_BOT_TOKEN': os.getenv('TELEGRAM_BOT_TOKEN'),
        'HUBSPOT_API_KEY': os.getenv('HUBSPOT_API_KEY'),
        'FLASK_DEBUG': os.getenv('FLASK_DEBUG', 'False') == 'True'
    }

    # Bot message templates
    MESSAGE_TEMPLATES = {
        'welcome': """
        Welcome to Arvea Elite! 🌟
        {distributor_name}'s Opportunity Opportunity
        
        Join our successful team and start your journey today!
        
        🎯 Benefits:
        - Financial Freedom
        - Flexible Schedule
        - Professional Training
        - Supportive Community
        
        Choose your path:
        """,
        
        'training_sequence': [
            {
                'day': 1,
                'subject': 'Quick Start Guide',
                'content': 'Here\'s how to begin your Arvea journey...'
            },
            {
                'day': 3,
                'subject': 'Building Your Network',
                'content': 'Learn the proven strategies for growing your team...'
            }
            # Add more training messages
        ]
    }
