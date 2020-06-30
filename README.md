# Flask: Getting Started

[Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

Minimal Application

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
      return 'Hello, World!'
      
Running flask application?

    $ export FLASK_APP=hello.py
    $ flask run

DEBUG=TRUE
so that you dont need to start the server over and over when there is a change

    $ export FLASK_DEBUG=1
    $ flask run


or add this 

    if __name__ == '__main__':
    app.run(host='127.0.0.1',port=4455,debug=True)   // Changed port number (Not needed)
    
Output:

<img width="615" alt="Screenshot 2020-06-29 at 9 02 02 PM" src="https://user-images.githubusercontent.com/11274840/86082110-d8277700-ba4b-11ea-8627-0c0da46af850.png">

