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

    profile_picture = db.Column(db.String(50), nullable=True)

    """Host's preferences for guest"""

    gender = db.Column(db.String(25), nullable=True)
    zip_code = db.Column(db.Integer, nullable=False)
    children = db.Column(db.Boolean, nullable=False)
    handicap_accessible = db.Column(db.Boolean, nullable=False)

    @classmethod
    def create_host(cls, email, first, last, password,
                    gender, zip_code, children, handicap_accessible):
        """Adding a new user to the db"""

        new_user = cls(email=email, first=first, last=last, password=password,
                       gender=gender, zip_code=zip_code, children=children,
                       handicap_accessible=handicap_accessible)

        db.session.add(new_user)
        db.session.commit()

    @classmethod
    def query_by_email(cls, email):
        """See if user email is already in system"""

        if cls.query.filter(cls.email == email).first() is not None:
            return True
        else:
            return False

    @classmethod
    def host_info_object(cls, email):
        """Return host info as object"""

        if cls.query_by_email(email) is not None:
            return cls.query.filter(cls.email == email).first()


class Host_Review(db.Model):
    """Review model for hosts"""

    __tablename__ = "host_reviews"

    host_review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    host_id = db.Column(db.Integer, db.ForeignKey('hosts.host_id'))
    host_review = db.Column(db.Text, nullable=False)

    host = db.relationship('Host', backref='host_reviews')

    @classmethod
    def create_host_review(cls, host_id, host_review):
        """Adding a new guest_review to the db"""

        review = cls(host_id=host_id, host_review=host_review)

        db.session.add(review)
        db.session.commit()


class Guest(db.Model):
    """Guest of STAYMORE"""

    __tablename__ = "guests"

    guest_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    first = db.Column(db.String(25), nullable=False)
    last = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)

    @classmethod
    def create_guest(cls, email, first, last, password,
                        gender, zip_code, children, handicap_accessible):
        """Adding a new user to the db"""

        new_user = cls(email=email, first=first, last=last, password=password,
                       gender=gender, zip_code=zip_code, children=children,
                       handicap_accessible=handicap_accessible)

        db.session.add(new_user)
        db.session.commit()

    @classmethod
    def query_by_email(cls, email):
        """See if user email is already in system"""

        if cls.query.filter(cls.email == email).first() is not None:
            return True
        else:
            return False

    @classmethod
    def guest_info_object(cls, email):
        """Return host info as object"""

        if cls.query_by_email(email) is not None:
            return cls.query.filter(cls.email == email).first()


class Guest_Review(db.Model):
    """Review model for guests"""

    __tablename__ = "guest_reviews"

    guest_review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.guest_id'))
    guest_review = db.Column(db.Text, nullable=False)

    guest = db.relationship('Guest', backref='guest_reviews')

    @classmethod
    def create_guest_review(cls, guest_id, guest_review):
        """Adding a new guest_review to the db"""

        review = cls(guest_id=guest_id, guest_review=guest_review)

        db.session.add(review)
        db.session.commit()


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