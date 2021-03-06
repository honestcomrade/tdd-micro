import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS

# the database is init'ed by SQL alchemy
# so we have tons of helper methods
db = SQLAlchemy()
toolbar = DebugToolbarExtension()


# Factory method of app
def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    CORS(app)

    # set up config from env var object
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    toolbar.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
