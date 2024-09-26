from app.DataBase import db

class sensor_data(db.Model):
        
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    equipment_id = db.Column(db.String(12), nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), nullable=False)
    value = db.Column(db.Numeric, nullable=False)  
        
    def toJson(self): 
        return {
            "id": self.id,
            "equipmentId": self.equipment_id,
            "timestamp": self.timestamp.isoformat(),  
            "value": float(self.value)
        }
            