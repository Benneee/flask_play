from distutils.command.config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskplay.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login' # Has to be the function name of our route to the login page
login_manager.login_message_category = 'info'

mail = Mail()


# Imported here to avoid circular import error since app is also imported in the routes file
# from flaskplay import routes


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskplay.users.routes import users
    from flaskplay.posts.routes import posts
    from flaskplay.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app


