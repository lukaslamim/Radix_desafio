from flask import Flask
from BD import sensorData

app = Flask(__name__)

@app.route('/sensor', methods=['GET'])
def getSensorData():
    return sensorData

app.run()
