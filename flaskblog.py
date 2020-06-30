from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about')
def about_author():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=4455,debug=True) 