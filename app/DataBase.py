from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def initDb(app):
    db.init_app(app)

