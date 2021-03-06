import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT, jwt_required

db = SQLAlchemy()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    db.init_app(app)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .user import UserAPI
    from .pet import PetAPI
    app.add_url_rule('/user', view_func=UserAPI.as_view('user'))
    app.add_url_rule('/pet', view_func=PetAPI.as_view('pet'))

    app.config['SECRET_KEY'] = 'super-secret'

    from petshop.user_model import authenticate, identity
    JWT(app, authenticate, identity)

    return app
