"""Models and databases for hack homelessness CALLED STAYMORE"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

##############################################################################


class Host(db.Model):
    """Host of STAYMORE"""

    __tablename__ = "hosts"

    host_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    first = db.Column(db.String(25), nullable=False)
    last = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)




class Guest(db.Model):
    """Guest of STAYMORE"""

    __tablename__ = "guests"

    guest_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    first = db.Column(db.String(25), nullable=False)
    last = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)

############################################################################

def init_app():
    from flask import Flask
    from server import app

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///staymore'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    #To utilize database interactively
    from flask import Flask
    from server import app

#FIXME!! Need to add to db.create_all() if it doesn't exist already

    connect_to_db(app)
    print "Connected to DB."