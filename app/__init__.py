from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Oh boy, here I go coding again'
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://vlbipskvftlutc:9ee870c6e357ba3e66f876d5d9c24a859b7461d874e60048b1adeebe15022355@ec2-54-152-175-141.compute-1.amazonaws.com:5432/drodqmn3a2jtq"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config.from_object(__name__)
db = SQLAlchemy(app)

from app import views, models