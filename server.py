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

    return render_template('homepage.html')


@app.route('/register_host')
def host_register():
    """Display register page"""

    return render_template('registerhost.html')


@app.route('/registerhost', methods=['POST'])
def register_host():
    """Process host's registration"""

    email = request.form['email']
    first = request.form['first']
    last = request.form['last']
    password = request.form['password']

    gender = request.form['gender']
    zip_code = request.form['zip_code']
    children = request.form['children']
    handicap_accessible = request.form['handicap_accessible']

    new_user = Host.create_host(email, first, last, password, gender,
                                zip_code, children, handicap_accessible)

    db.session.add(new_user)
    db.session.commit()

    return "Hi"

@app.route ('/hostprofile')
def host_profile():
    """Display host profile"""

    return render_template("hostprofile.html")


@app.route('/registerguest')
def register_guest():
    """Process guest's registration"""

    email = request.form['email']
    first = request.form['first']
    last = request.form['last']
    password = request.form['password']

    gender = request.form['gender']
    zip_code = request.form['zip_code']
    children = request.form['children']
    handicap_accessible = request.form['handicap_accessible']

    new_user = Guest.create_guest(email, first, last, password, gender,
                                zip_code, children, handicap_accessible)

    db.session.add(new_user)
    db.session.commit()

    return "Hi"


@app.route('/login', methods=['POST'])
def user_login():
    """Process the login and redirect user to dashboard"""

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

@app.route('/aboutus')
def display_aboutus():

    return render_template('aboutus.html')

@app.route('/hdashboard')
def display_dashboard():

    return render_template('hostdashboard.html')

@app.route('/pdashboard')
def partner_dashboard():

    return render_template('partnerdashboard.html')



if __name__ == "__main__":

    app.debug = True
    DebugToolbarExtension(app)
    connect_to_db(app)


    app.run(host="0.0.0.0")
