from flask import Flask, render_template, request, flash, session, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Host, Guest

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

    return render_template('base.html')


# @app.route('/register_partner')
# def guest_registration():

    return "FIX ME"


# @app.route('/register_host')
# def host_registration():


#     return "FIX ME"

@app.route('/login', methods=['POST'])
def user_login():
    """Process the login and redirect user to dashboard"""

<<<<<<< HEAD
    email = request.form['user[username]']
    password = request.form['user[password]']

    if Host.query_by_email(email) or Guest.query_by_email(email) is True:
        if Host.query_by_email(email):
            if (Host.host_info_object(email)).password != password:
                return "Wrong password"
            else:
                session['user_id'] = (Host.host_info_object(email)).host_id
                return "Logged In"
        if Guest.query_by_email(email):
            if (Guest.guest_info_object(email)).password != password:
                return "Wrong password"
            else:
                session['user_id'] = (Guest.guest_info_object(email)).guest_id
                return "Logged In"

    return "FIX ME"

=======
@app.route('/dashboard')
def display_dashboard():

    return render_template('hostdashboard.html')


# @app.route('/partners')
# def display_partners():

#     return "FIX ME"
>>>>>>> 88f5720a94d84b866bb7056c1e0f84b7d7bd210e

if __name__ == "__main__":

    app.debug = True
    DebugToolbarExtension(app)
    connect_to_db(app)


    app.run(host="0.0.0.0")