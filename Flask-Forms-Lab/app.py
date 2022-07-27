import re
from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

from importlib_metadata import method_cache


app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

app.config['SECRET_KEY'] = 'THEMOSTSECRETKEYPOSSIBLE'

username = "watan"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		if request.form['username'] == username and request.form['password'] == password:
			return render_template('home.html', facebook_friends = facebook_friends, username = username)
		else:
			return render_template("404.html")
	else:
			return render_template('login.html')



  
@app.route('/home',  methods=['GET', 'POST'])  # '/' for the default page
def home():
	return render_template('home.html', facebook_friends = facebook_friends, username = username)





@app.route('/friend_exist/<string:name>',methods=['GET', 'POST'])  # '/' for the default page
def friend_exist(name):
	return render_template('friend_exists.html', n = name)





if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)