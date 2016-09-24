from flask import Flask, render_template, request, flash, session, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from jinja2 import StrictUndefined


#app variable binding for argument in connect_to_db function in model
app = Flask(__name__)


#added for Flask sessions and debugtoolbar use
app.secret_key = "ABC"
#to raise an error in Jinja2 so it can't pass silently
app.jinja_env.undefined = StrictUndefined
#bypasses bug that results in server restart for each update to jinja template
app.jinja_env.auto_reload = True


@app.route('/')
def index():
    """Homepage"""


    return render_template('homepage.html')


@app.route('/register_guest')
def guest_registration():

    return "FIX ME"


@app.route('/register_host')
def host_registration():


    return "FIX ME"

@app.route('/login')
def user_login():


    return "FIX ME"


@app.route('/dashboard')
def display_dashboard():


    return "FIX ME"


@app.route('/partners')
def display_partners():

    return "FIX ME"

if __name__ == "__main__":

    # app.debug = True
    # connect_to_db(app)
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")