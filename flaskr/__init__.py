import os

from flask import Flask
from flask_cors import CORS
from flaskr.baseinit import init as initBase
from flaskr.score import scorecontroller


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI="sqlite:////home/sarwas/test.db",
    )

    initBase()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flaskr.card import cardcontroler
    app.register_blueprint(cardcontroler.bp)
    app.register_blueprint(scorecontroller.bp)
    return app
