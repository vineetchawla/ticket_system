# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ticket_app import db, login_manager

class User(UserMixin, db.Model):
    """
    Create an User table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.first_name)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class ticket(db.model):
    """
    contains all the ticket data
    the email links to the user email
    """

    ticket_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticket_name = db.Column(db.String(60))
    ticket_email = db.Column(db.String(60))
    subject = db.Column(db.String(150))
    type = db.Column(db.String(15))
    urgency = db.Column(db.String(15))
    message = db.Column(db.String(500))
    time = db.Column(db.DateTime)


    def __repr__(self):
        return '<ID: {}>'.format(self.ticket_id)