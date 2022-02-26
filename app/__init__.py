from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    # app.config.from_pyfile('config.py')

    # Initializing Flask Extensions
    bootstrap.init_app(app)

    # Will add the views and forms

    return app

        # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)

    return app
# from app import views
# from app import error