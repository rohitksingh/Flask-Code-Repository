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

## How to resolve Server is already in use error?

    kill -9 `lsof -i:5000 -t`





How to add Login Page?

- Create Python class 
- Add {{form.username(class="form-control form-control-lg")}}
- Add methods=['GET', 'POST'] in register route
- Adding Flash message


## After App Restrucure 

<img width="300" alt="Screenshot 2020-07-03 at 4 44 24 PM" src="https://user-images.githubusercontent.com/11274840/86501310-9567e680-bd4c-11ea-8032-fd35b48adb65.png">


 </br></br>
## About author
<p align="center">This Repository is developed and maintained by </p>
<p align="center">
  <a href="https://stackoverflow.com/users/4700156/rohit-singh?tab=profile"><img width="100" height="100" src="https://user-images.githubusercontent.com/11274840/30627155-38952a30-9dec-11e7-9072-a00d9a86bdb8.gif">
</p></a>
<a href="https://stackoverflow.com/users/4700156/rohit-singh?tab=profile">
<p align="center">
  Rohit Singh
</p>
</a>
