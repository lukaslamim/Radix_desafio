from flask import Flask
from app.routes.SensorDataRoute import register_routes
from app.DataBase import initDb


def createApp():
    
    app = Flask(__name__)
    
    app.config['JSON_SORT_KEYS'] = False
    # IN LOCALHOST
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lukas:741852@localhost:5432/sensor_database'  # Substitua conforme necessário
    # IN CONTAINER
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lukas:741852@db:5432/sensor_database'
    initDb(app)
    
    register_routes(app)
    
    return app