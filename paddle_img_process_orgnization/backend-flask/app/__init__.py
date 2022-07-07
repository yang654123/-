from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER 
    app.template_folder = config_class.TEMPLATE_FOLDER

    db.init_app(app)

    # blueprint registration
    from app.Controller.errors import bp_errors as errors
    app.register_blueprint(errors)

    from app.Controller.routes import bp_routes as routes
    app.register_blueprint(routes)

    from app.Controller.user import authentication_blueprint as authentication
    app.register_blueprint(authentication)

    # from app.Controller.comments import comments_blueprint as comments
    # app.register_blueprint(comments)

    if not app.debug and not app.testing:
        pass
        # ... no changes to logging setup

    return app
