import os
from app import app
from . import db
from app.models import UserProfile
from flask import render_template, request, redirect, url_for, flash
from app.forms import ProfileForm
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CsrfProtect
CsrfProtect(app)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/profile', methods=['GET','POST'])
def profile():
	form = ProfileForm()
	if form.validate_on_submit() and request.method == 'POST':
		file = request.files['upload']
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		img_address = "/static/uploads/"+filename
		user = UserProfile(request.form['firstname'], request.form['lastname'], request.form['gender'], request.form['email'], request.form['location'], request.form['biography'], img_address)
		db.session.add(user)
		db.session.commit() 
		flash('New profile was successfully added')
		return redirect(url_for('profiles'))
	return render_template('profile.html', form=form)

@app.route('/profiles')
def profiles():
	profiles = db.session.query(UserProfile).all() 
	return render_template('profiles.html', profiles=profiles)

@app.route('/profile/<int:id>')
def specific_profile(id):
	profile = UserProfile.query.get(id)
	return render_template('specific_profile.html', profile=profile)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8080) 