from flask import Flask, render_template, request, redirect, url_for, session
    from app.config import APP_CONFIG
    from app.hubspot_sync import HubSpotSync
    from app.bot_handler import ArveaBot
    from app.auth import login_required
    from werkzeug.security import generate_password_hash, check_password_hash

    app = Flask(__name__)
    app.secret_key = APP_CONFIG['SECRET_KEY']
    app.debug = APP_CONFIG['FLASK_DEBUG']

    hubspot = HubSpotSync(APP_CONFIG['HUBSPOT_API_KEY'])
    bot = ArveaBot(APP_CONFIG['TELEGRAM_BOT_TOKEN'])
    bot.updater.start_polling()

    @app.route('/')
    def landing():
        return render_template('landing.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            # Replace with actual authentication logic
            if username == 'admin' and check_password_hash(generate_password_hash('password'), password):
                session['user_id'] = 1
                session['role'] = 'admin'
                return redirect(url_for('admin_dashboard'))
            elif username == 'distributor' and check_password_hash(generate_password_hash('password'), password):
                session['user_id'] = 2
                session['role'] = 'distributor'
                return redirect(url_for('distributor_dashboard'))
            else:
                return render_template('login.html', error='Invalid credentials')
        return render_template('login.html')

    @app.route('/admin')
    @login_required
    def admin_dashboard():
        if session.get('role') != 'admin':
            return redirect(url_for('distributor_dashboard'))
        return render_template('admin_dashboard.html')

    @app.route('/distributor')
    @login_required
    def distributor_dashboard():
        if session.get('role') != 'distributor':
            return redirect(url_for('admin_dashboard'))
        return render_template('distributor_dashboard.html')

    @app.route('/logout')
    def logout():
        session.pop('user_id', None)
        session.pop('role', None)
        return redirect(url_for('login'))
