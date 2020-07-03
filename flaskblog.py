from flask import Flask, render_template, url_for, flash, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oowewbcdeoproeporpebcoiffoekcjefdcdcndcoidfcbdc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(20), unique = True, nullable = False)
    image_file = db.Column(db.String(20),  nullable = False, default="default.jpg")
    password = db.Column(db.String(20), nullable = False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, unique = True, nullable = False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

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

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=4455,debug=True) 