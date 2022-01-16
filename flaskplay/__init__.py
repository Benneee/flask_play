import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '2cbaca196d94f099372f70ede31a6351'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # For a local copy of sqlite
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Has to be the function name of our route to the login page
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

mail = Mail(app)


# Imported here to avoid circular import error since app is also imported in the routes file
from flaskplay import routes

