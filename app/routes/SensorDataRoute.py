from flask import request, make_response, render_template
from app.models.SensorDataModel import sensor_data
from app.services import Services
from app.services import SensorDataService
from app.DataBase import db
import datetime

def RegisterSensorDataRoutes(app):

    #select all data
    @app.route('/sensor/data/all', methods = ['GET'])
    def SelectAllData():

        sensorData = SensorDataService.listToJson(sensor_data.query.all())

        if len(sensorData) == 0:
            return make_response({"Error": "no data"}, 404 )
        
        return Services.createResponse(sensorData, 200)

    #select by equipment_id
    @app.route('/sensor/<equipment_id>/data', methods = ['GET'])
    def SelectDataByequipmentId(equipment_id): 
        
        sensorData = SensorDataService.listToJson(sensor_data.query.filter_by(equipment_id=equipment_id))

        if len(sensorData) > 0:
            return Services.createResponse(sensorData, 200)
        
        return make_response({"Error": "Sensor not found"}, 404)
                                        
    #insert sensor data
    @app.route('/sensor/data', methods = ['POST'])
    def InsertDataSensor(): 
        
        body = request.get_json()
        
        if not SensorDataService.ValidBody(body):
            return make_response({"Error": "Invalid data, 'equipmentId', 'timestamp' and/or 'value' are Invalid."}, 400)
        try:
            sensorData = sensor_data(equipment_id = body['equipmentId'], timestamp = body['timestamp'], value = body['value'])
            db.session.add(sensorData)
            db.session.commit()
            
            return Services.createResponse(sensorData.toJson(), 201)
        
        except Exception as e:
            return make_response({"Error": f"Unable to create: {str(e)}" }, 400)
    
    #select by date
    @app.route('/sensor/data/average', methods=['GET'])
    def get_average_sensor_data():
        try:
            averages = {
                "last_24_hours": SensorDataService.Average.getAverage24h(),
                "last_48_hours": SensorDataService.Average.getAverage48h(),
                "last_week": SensorDataService.Average.getAverage7d(),
                "last_month": SensorDataService.Average.getAverage30d()
            }
            return Services.createResponse(averages, 200)
        
        except Exception as e:
            return make_response({'Error': 'Erro ao tentar obter dados ' + str(e)}, 500)

    #to do
    #UpdateData
    #DeleteData
    
    @app.route('/sensor/data/csv', methods=['POST'])
    def UploadCsv():
        #decode and split data
        if request.data.decode('utf-8', errors='replace').find('\n\r') > 0:    
            reader = request.data.decode('utf-8', errors='replace').split('\n\r')
            
        elif request.data.decode('utf-8', errors='replace').find('\r\n') > 0:       
            reader = request.data.decode('utf-8', errors='replace').split('\r\n')
            
        elif request.data.decode('utf-8', errors='replace').find('\n') > 0:    
            reader = request.data.decode('utf-8', errors='replace').split('\n')
            
        elif request.data.decode('utf-8', errors='replace').find('\r') > 0:       
            reader = request.data.decode('utf-8', errors='replace').split('\r')
        
        #validacoes
        for idx, row in enumerate(reader):
                
            if idx != 0 and len(row) != 0:
                if row.find(';') > 0:
                    subRows = row.split(';')
                else:
                    subRows = row.split(',')
                
                
                if len(subRows) != 3:
                    return make_response({"Invalid Line": "Missing or extra data, on line: " + str(idx + 1)}, 400)
                
                for subIdx, subRow in enumerate(subRows):
                    #valid line
                    if len(subRow) == 0: 
                        return make_response({"Invalid line": "Line number: " + str(idx + 1)  + + " colunm number: " + str(subIdx + 1) + " has blank field"}, 400)  
                    
                    #valid format
                    #equipment_id
                    if subIdx == 0:
                        if not subRow.startswith("EQ-"):
                            return make_response({"Invalid data": "Invalide data equipment_id, on line number: " + str(idx + 1) + ' equipment_id most start with EQ-'}, 400) 
                    #timestamp    
                    elif subIdx == 1:
                        try:
                            timestamp = datetime.datetime.strptime(subRow, "%Y-%m-%dT%H:%M:%S.%f%z")
                            timestamp.isoformat() 
                        except Exception as e:
                            return make_response({"Invalid data": "Invalide data timestamp, on line number: " + str(idx + 1) 
                                                + ' data is not in ISO format, correct exemple: ' + '2023-02-12T01:30:00.000-05:00'}, 400)   
                    #value      
                    elif subIdx == 2:
                        try:
                            float(subRow)
                        except ValueError:
                            return make_response({"Invalid data": "Invalide data value, on line number: " + str(idx + 1) + ' not possible to convert to numeric'}, 400) 
                
                try:
                    sensorData = sensor_data(equipment_id=subRows[0], timestamp=subRows[1], value=subRows[2])        
                    db.session.add(sensorData)
                    db.session.flush()
                except Exception as e:
                    return make_response({"Error": f"Unable to add into database: {str(e)}" }, 400)
                
            elif len(row) != 0: 
                #valid header
                if row != 'equipmentId;timestamp;value':
                    return make_response({"Error": "Invalid header, most be: equipmentId;timestamp;value, instead it is: " + row}, 400)
    
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return make_response({"Error": f"Unable to finish request: {str(e)}" }, 400)
        
        return make_response({"Message": "all Data inserted successfully."}, 201) 
    
    #HTML
    @app.route('/')
    def index():
        return render_template('Index.html')        