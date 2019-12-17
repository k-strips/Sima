#Importing flask dependencies for handling views
from flask import Blueprint, g, render_template, url_for, \
flash, redirect, request

#importing database from app
from app import db

#importing forms from web forms
#from app.web.forms import contact

web = Blueprint("web", __name__, template_folder="templates", static_folder='static')

@web.route('/')
@web.route('/home')
def home():
    return render_template("web/pages/home.html")

@web.route('/about')
def about():
    return render_template("web/pages/about.html")

@web.route('/attornies')
def attornies():
    return render_template("web/pages/attornies.html")

@web.route('/attorney')
def attorney():
    return render_template("web/pages/attorney.html")

@web.route('/careers')
def careers():
    return render_template("web/pages/careers.html")

@web.route('/contact')
def contact():
    return render_template("web/pages/contact.html")
