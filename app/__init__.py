from flask import Flask
from .extensions import db, migrate, ma, cors
from .config import Config
from .Notes.routes import notes_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app, resources={r"/*":{"origins":"*"}})

    app.register_blueprint(notes_api)

    return app