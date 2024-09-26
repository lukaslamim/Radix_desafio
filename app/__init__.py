from flask import Flask
from app.DataBase import initDb
from app.Auth import initAuth
from app.routes.RouteRegistrer import RouteRegistrer

def createApp():
    
    app = Flask(__name__)
    
    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lukas:741852@db:5432/sensor_database'
    
    initDb(app)
    
    RouteRegistrer(app)
    
    #implementado
    #initAuth(app)
    
    return app