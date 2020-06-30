from flask import Flask, render_template
app = Flask(__name__)

posts = [
            {
                'author': 'Rohit',
                'tittle': 'First Blog post',
                'content': 'First blog post content. This is the dummy content',
                'date_posted': '29 June 2020'

            },
            {
                'author': 'Jon Doe',
                'tittle': 'Second Blog post',
                'content': 'Second blog post content. This is the second content',
                'date_posted': '2 June 2020'

            }
]

@app.route('/home')
@app.route('/')
def hello_world():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about_author():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=4455,debug=True) 