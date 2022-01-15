from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '2cbaca196d94f099372f70ede31a6351'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # For a local copy of sqlite
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # use utcnow so dates can be consistent
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Post('{self.title}', '{self.date_posted}')"


# Dummy data
title = 'About'
posts = [
    {
        'id': 1,
        'author': 'Ben McGregor',
        'title': 'Lorem 1',
        'content': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magni similique earum expedita facilis    unde aspernatur rem alias praesentium nam exercitationem quis ex illum, dicta vero quia placeat labore, ad facere, et tenetur id laborum rerum quam. Adipisci possimus quisquam esse corrupti reiciendis?',
        'created_at': 'January 12, 2021'
    },
    {
        'id': 2,
        'author': 'Ewan Roberts',
        'title': 'Lorem 2',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum unde enim ipsam cumque? Repellendus, perspiciatis veniam at doloribus, officiis aut explicabo porro voluptatum numquam non minus inventore? Adipisci aliquid voluptas, repellat mollitia incidunt vitae exercitationem aut numquam amet magnam enim ex tenetur, molestias labore unde? Ipsum, perferendis inventore. Quasi, dignissimos.',
        'created_at': 'January 10, 2021'
    },
    {
        'id': 3,
        'author': 'Ben Marcus',
        'title': 'Lorem 3',
        'content': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magni similique earum expedita facilis    unde aspernatur rem alias praesentium nam exercitationem quis ex illum, dicta vero quia placeat labore, ad facere, et tenetur id laborum rerum quam. Adipisci possimus quisquam esse corrupti',
        'created_at': 'January 8, 2021'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # Validation
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)