from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
            {
                'author': 'Rohit',
                'tittle': 'First Blog post',
                'content': 'First blog post content. This is the dummy content',
                'date_posted': '29 June 2020',
                'color': 'bg-primary'

            },
            {
                'author': 'Jon Doe',
                'tittle': 'Second Blog post',
                'content': 'Second blog post content. This is the second content',
                'date_posted': '2 June 2020',
                'color': 'bg-success'

            },
            {
                'author': 'Jon Wick',
                'tittle': 'Thord Blog post',
                'content': 'Third blog post content. This is the second content',
                'date_posted': '21 June 2020',
                'color': 'bg-warning'

            }
]

colors =['bg-primary', 'bg-success', 'bg-warning', 'bg-dark']

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about_author():
    return render_template('about.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'user@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful', 'warning')    
    return render_template('login.html', form=form)   