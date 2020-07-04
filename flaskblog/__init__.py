from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oowewbcdeoproeporpebcoiffoekcjefdcdcndcoidfcbdc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
brcypt = Bcrypt(app)

from flaskblog import routes