from flask import flask render_template , redirect , url_for , request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user 
import pyttsx3

#Starting the Flask App
app = Flask(_app.py_)
app.config["Secret_key"] = "bdfe5f3338318579b6b0357f15aa0ea238c9951ec8cb10a2dae87c6ed5b08a40"
app.config["SQLALCHEMY_DATABASE_URL"] = sqlite:
db = SQLAlchemy(app)

#Starting the Flask Login
