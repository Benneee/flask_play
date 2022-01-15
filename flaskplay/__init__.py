from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '2cbaca196d94f099372f70ede31a6351'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # For a local copy of sqlite
db = SQLAlchemy(app)

# Imported here to avoid circular import error since app is also imported in the routes file
from flaskplay import routes

