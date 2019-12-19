#import flask and template operators
from flask import Flask, g

#import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

#import Bcrypt to has passwords
from flask_bcrypt import Bcrypt

#import flask login extention to handle users
from flask_login import LoginManager

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy()

#define bycrypt object
bcrypt = Bcrypt()

#define login manager object
login_manager = LoginManager()

def create_app():

    #define wsgi application object
    app = Flask(__name__, instance_relative_config=True)

    #Load the default configuration
    app.config.from_object('config.default')

    #Load configuration from the instance folder
    app.config.from_pyfile('config.py')

    #Load the configuration from env
    app.config.from_envvar('APP_CONFIG')

    #initialize Plugins
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():

        # Import a module / component using its blueprint handler variable
        from app.admin.views import admin
        from app.web.views import web

        #register blueprints
        app.register_blueprint(admin)
        app.register_blueprint(web)

        # Build the database:
        # This will create the database file using SQLAlchemy
        db.create_all()

        return app
