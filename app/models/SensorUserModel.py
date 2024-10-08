from app.DataBase import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class sensor_user(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)