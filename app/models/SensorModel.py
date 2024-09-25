from app.DataBase import db

class Sensor(db.Model):
        
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    equipment_id = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), nullable=False, default=db.func.now())
    value = db.Column(db.Numeric, nullable=False)  
        
    def toJson(self): 
        return {
            "id": self.id,
            "equipment_id": self.equipment_id,
            "timestamp": self.timestamp.isoformat(),  
            "value": float(self.value)
        }
            