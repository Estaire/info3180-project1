from . import db
import datetime

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(80))
    biography = db.Column(db.String(80))
    img_address = db.Column(db.String(120))
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, first_name, last_name, gender, email, location, biography, img_address):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.img_address = img_address
        self.created_on = datetime.datetime.now()

    def get_id(self):
        try:
            return unicode(self.id) 
        except NameError:
            return str(self.id)

    def __repr__(self):
        return f"<id={self.id}, first_name={self.first_name}, last_name={self.last_name}, gender={self.gender}, email={self.email}, location={self.location}, biography={self.biography}, img_address={self.img_address}, created_on={self.created_on}>"

