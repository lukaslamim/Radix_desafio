from flask_bcrypt import Bcrypt
from app.models.SensorUserModel import bcrypt

auth = Bcrypt

def initAuth(app):
    auth.init_app(bcrypt, app)
