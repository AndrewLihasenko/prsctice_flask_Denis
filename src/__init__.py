from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from src.routes.tables import tables
from src.config import *
from src.routes.restaurant import restaurant


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}'
    with app.app_context():
        app.register_blueprint(restaurant)
        # app.register_blueprint(tables)
        return app

def create_db(app):
    return SQLAlchemy(app)

app = create_app()
db = create_db(app)
