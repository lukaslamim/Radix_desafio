from flask import Flask, Request, Response, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lukas:741852@localhost:5432/sensor_database'

db = SQLAlchemy(app)

#create sensor model
class sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    equipmentid = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)  
    value = db.Column(db.Numeric, nullable=False)  
    
    def toJson(self):
        return {
            "id": self.id,
            "equipmentId": self.equipmentid,
            "timestamp": self.timestamp.isoformat(),  
            "value": float(self.value)  
        }
        
def listToJson(List):
    return [object.toJson() for object in List]
        
def createResponse(content):
    return make_response(
        jsonify(
        content
        )
    )    

#select all
@app.route('/sensors', methods = ['GET'])
def SelectAll():
    return createResponse(listToJson(sensor.query.all()))

#select by id
@app.route('/sensor/id', methods = ['GET'])
def SelectById(id):
    return createResponse(listToJson(sensor.query))

app.run()
