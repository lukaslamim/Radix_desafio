
from datetime import datetime, timedelta
from sqlalchemy import func
from app.models.SensorDataModel import sensor_data
from app.DataBase import db

class Average:
    @staticmethod
    def get_average_for_last_24_hours():
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=24)

        results = (
            db.session.query(
                sensor_data.equipment_id.label('equipment_id'),  # Agrupa por equipment_id
                func.date(sensor_data.timestamp).label('date'),  # Agrupa por data
                func.avg(sensor_data.value).label('average')     # Calcula a média
            )
            .filter(sensor_data.timestamp >= start_time)
            .filter(sensor_data.timestamp <= end_time)
            .group_by(sensor_data.equipment_id, func.date(sensor_data.timestamp))
            .order_by(sensor_data.equipment_id, func.date(sensor_data.timestamp))  
            .all()
        )

        return [{'equipment_id': result.equipment_id, 'timestamp': result.date.isoformat(), 'average': result.average} for result in results]

    @staticmethod
    def get_average_for_last_48_hours():
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=48)

        results = (
            db.session.query(
                sensor_data.equipment_id.label('equipment_id'),  # Agrupa por equipment_id
                func.date(sensor_data.timestamp).label('date'),  # Agrupa por data
                func.avg(sensor_data.value).label('average')     # Calcula a média
            )
            .filter(sensor_data.timestamp >= start_time)
            .filter(sensor_data.timestamp <= end_time)
            .group_by(sensor_data.equipment_id, func.date(sensor_data.timestamp))
            .order_by(sensor_data.equipment_id, func.date(sensor_data.timestamp))  
            .all()
        )

        return [{'equipment_id': result.equipment_id, 'timestamp': result.date.isoformat(), 'average': result.average} for result in results]

    @staticmethod
    def get_average_for_last_week():
        end_time = datetime.now()
        start_time = end_time - timedelta(weeks=1)

        results = (
            db.session.query(
                sensor_data.equipment_id.label('equipment_id'),  # Agrupa por equipment_id
                func.date(sensor_data.timestamp).label('date'),  # Agrupa por data
                func.avg(sensor_data.value).label('average')     # Calcula a média
            )
            .filter(sensor_data.timestamp >= start_time)
            .filter(sensor_data.timestamp <= end_time)
            .group_by(sensor_data.equipment_id, func.date(sensor_data.timestamp))
            .order_by(sensor_data.equipment_id, func.date(sensor_data.timestamp))  
            .all()
        )

        return [{'equipment_id': result.equipment_id, 'timestamp': result.date.isoformat(), 'average': result.average} for result in results]

    @staticmethod
    def get_average_for_last_month():
        end_time = datetime.now()
        start_time = end_time - timedelta(days=30)

        results = (
            db.session.query(
                sensor_data.equipment_id.label('equipment_id'),  # Agrupa por equipment_id
                func.date(sensor_data.timestamp).label('date'),  # Agrupa por data
                func.avg(sensor_data.value).label('average')     # Calcula a média
            )
            .filter(sensor_data.timestamp >= start_time)
            .filter(sensor_data.timestamp <= end_time)
            .group_by(sensor_data.equipment_id, func.date(sensor_data.timestamp))
            .order_by(sensor_data.equipment_id, func.date(sensor_data.timestamp))  
            .all()
        )

        return [{'equipment_id': result.equipment_id, 'timestamp': result.date.isoformat(), 'average': result.average} for result in results]



def listToJson(List):
    return [sensorData.toJson() for sensorData in List]


def ValidBody(body):

    if ('equipmentId' not in body or 'value' not in body or 'timestamp' not in body
            or not body['equipmentId'].startswith("EQ-")):
        return False
    try:
        float(body['value'])
    except ValueError:
        return False
    try:
        timestamp = datetime.strptime(body['timestamp'], "%Y-%m-%dT%H:%M:%S.%f%z")
        timestamp.isoformat() 
    except Exception:
        return False
    
    return True
           