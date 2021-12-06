#!/usr/bin/env python

import os

from flask import Flask


def create_app(test_config=None):
    # Initialise the application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY"),
        DATABASE=os.path.join(app.instance_path, os.environ.get("DATABASE")),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialise the database
    from . import database

    database.init_app(app)

    # Initialise user
    from . import user

    app.register_blueprint(user.blueprint)

    # Initialise cast
    from . import cast

    app.register_blueprint(cast.blueprint)

    @app.route("/")
    def index():
        return "Notecast"

    return app
