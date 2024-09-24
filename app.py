from flask import Flask
from BD import sensors

app = Flask(__name__)

@app.route('/sensor', methods=['GET'])
def getSensorData():
    return sensors

app.run()
