from flask import Flask, render_template, url_for
from forms import LoginForm, RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'oowewbcdeoproeporpebcoiffoekcjefdcdcndcoidfcbdc'

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
def hello_world():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about_author():
    return render_template('about.html')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)        

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=4455,debug=True) 