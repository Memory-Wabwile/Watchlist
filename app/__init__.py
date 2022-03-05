from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_simplemde import SimpleMDE


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


bootstrap = Bootstrap()
db = SQLAlchemy()  #first import SQLAlchemy then create a db instance

simple = SimpleMDE()

def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    # app.config.from_pyfile('config.py')

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)        # call the init method and pass the app instance
    login_manager.init_app(app)

    # Will add the views and forms

    return app

        # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
    simple.init_app(app)

    return app
# from app import views
# from app import error