from flask import render_template, url_for, flash, redirect, request

from flaskplay import app, db, bcrypt
from flaskplay.forms import RegistrationForm, LoginForm
from flaskplay.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    # Validation
    if form.validate_on_submit():
        # First, we hash the password
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Create an instance of the User object using the information from the form
        user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        # Save in the DB
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Profile')
