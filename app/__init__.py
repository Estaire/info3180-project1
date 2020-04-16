from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Oh boy, here I go coding again'
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password123@localhost/profiles"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config.from_object(__name__)
db = SQLAlchemy(app)

from app import views, models