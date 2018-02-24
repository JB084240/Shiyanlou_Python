from flask import Flask, render_template
from simpledu2.config import configs
from simpledu2.models import db, Course, User


def register_blueprints(app):
    from .handlers import front, course, admin
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)

def create_app(config):
    
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprints(app)

    return app

