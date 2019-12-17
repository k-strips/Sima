#impot database from app and bcrypt
from app import db, bcrypt

#import sqlalchemy hybrid_property
from sqlalchemy.ext.hybrid import hybrid_property


#create admin Model
class Admin(db.Model):

    __tablename__='admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(90), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    _password = db.Column(db.String(128), nullable=False)

    #New class instance
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self._password = password

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

    def __repr__(self):
        return f"{self.name}"


class Lawyer(db.Model):

    __tablename__="lawyers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    position = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.String(1000), nullable=True)
    expectise = db.Column(db.String(40), nullable=False)
    education = db.Column(db.String(50), nullable=True)

    #New Lawyer instance
    def __init__(self, name, position, phone, email):
        self.name = name
        self.position = position
        self.phone = phone
        self.email = email
        self.bio = " "
        self.expectise = []
        self.education = " "


    #method to add area of legal expectise
    def add_bio(self, bio):
        self.expectise.append(bio)

    #method to add eexpectise
    def add_expectise(self, expectise):
        self.expectise.append(expectise)

    #method to add education
    def add_education(self, education):
        self.education.append(education)

    def __repr__(self):
        return f"Name: {self.name} \n tel: {self.phone} \
         \n Email: {self.email}"
