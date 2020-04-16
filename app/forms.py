from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed, FileRequired

class ProfileForm(FlaskForm):
	firstname = StringField('First Name',validators=[DataRequired()])
	lastname = StringField('Last Name',validators=[DataRequired()])
	gender = SelectField('Gender', choices=[('Male','Male'),('Female','Female')],validators=[DataRequired()])
	email = StringField('E-mail',validators=[DataRequired()])
	location = StringField('Location',validators=[DataRequired()])
	biography = StringField('Biography', widget=TextArea())
	upload = FileField('Browse...', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])