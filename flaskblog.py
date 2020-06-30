from flask import Flask
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def hello_world():
    return "Hi there how you doing? I am doing great"

@app.route('/about')
def about_author():
    return "Hi there how you doing? I am doing great"    

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=4455,debug=True) 