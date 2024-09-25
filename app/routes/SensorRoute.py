from flask import request, make_response
from app.models.SensorModel import Sensor
from app.services import Services
from app.services import SensorService
from app.DataBase import db
import datetime

def register_routes(app):
        
    #select all
    @app.route('/sensors/data', methods = ['GET'])
    def SelectAll():

        sensorsJson = SensorService.listToJson(Sensor.query.all())

        if len(sensorsJson) == 0:
            return make_response({"Error": "no data"}, 404 )
        
        return Services.createResponse(sensorsJson, 200)

    #select by equipment_id
    @app.route('/sensor/data/<equipment_id>', methods = ['GET'])
    def SelectByequipmentId(equipment_id): 
        
        sensor = SensorService.listToJson(Sensor.query.filter_by(equipment_id=equipment_id))

        if len(sensor) > 0:
            return Services.createResponse(sensor, 200)
        
        return make_response({"Error": "Sensor not found"}, 404)
                                        
    #InsertData
    @app.route('/sensor/data', methods = ['POST'])
    def InsertDataSensor(): 
        
        body = request.get_json()
        
        if not SensorService.ValidBody(body):
            return make_response({"Error": "Invalid data, 'equipment_id' and/or 'value' are Invalid."}, 400)
        try:
            newSensor = Sensor(equipment_id = body['equipment_id'], value = body['value'])
            db.session.add(newSensor)
            db.session.commit()
            
            return Services.createResponse(newSensor.toJson(), 201)
        
        except Exception as e:
            return make_response({"Error": f"Unable to create: {str(e)}" }, 400)
    
    
    #to do
    #UpdateData
    #DeleteData
    
    @app.route('/sensors/data/upload_csv', methods=['POST'])
    def UploadCsv():
        
        if request.data.decode('utf-8').find(';') == -1:
            reader = request.data.decode('utf-8').split(',')
        else:
            reader = request.data.decode('utf-8').split(';')

        reader = request.data.decode('utf-8').split('\n')
        
        #validacoes
        for idx, row in enumerate(reader):
            
            if idx != 0:
                if row.find(';') == -1:
                    subRows = row.split(',')
                else:
                    subRows = row.split(';')
                
                
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
                            return make_response({"Invalid data": "Invalide data equipment_id, on line number: " + str(idx + 1)}, 400) 
                    #timestamp    
                    elif subIdx == 1:
                        try:
                            timestamp = datetime.datetime.strptime(subRow, "%Y-%m-%dT%H:%M:%S.%f%z")
                            timestamp.isoformat() 
                        except Exception as e:
                            return make_response({"Invalid data": "Invalide data timestamp, on line number: " + str(idx + 1) 
                                                + ' data is not in iso format, correct exemple: ' + '2023-02-12T01:30:00.000-05:00;78.8'}, 400)   
                    #value      
                    elif subIdx == 2:
                        try:
                            float(subRow)
                        except ValueError:
                            return make_response({"Invalid data": "Invalide data value, on line number: " + str(idx + 1)}, 400) 
                
                try:
                    sensor = Sensor(equipment_id=subRows[0], timestamp=subRows[1], value=subRows[2])        
                    db.session.add(sensor)
                except Exception as e:
                    return make_response({"Error": f"Unable to add into database: {str(e)}" }, 400)
                
            else: 
                #valid header
                if row != 'equipmentId;timestamp;value':
                    return make_response({"Error": "Invalid header, most be: equipmentId;timestamp;value, instead it is: " + row}, 400)
    
        try:
            db.session.commit()
        except Exception as e:
            return make_response({"Error": f"Unable to finish request: {str(e)}" }, 400)
        
        return make_response({"Message": "all Data inserted successfully."}, 201) 