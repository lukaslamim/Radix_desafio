import unittest
from app import createApp
from app.services.SensorDataService import Average
from app.DataBase import db
from app.models.SensorDataModel import sensor_data

class TestAverageService(unittest.TestCase):
    def setUp(self):
        self.app = createApp()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all() 

        self.add_test_data()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def add_test_data(self):
        for i in range(5):
            db.session.add(sensor_data(equipment_id=f'EQ-{i}', timestamp='2023-0112T01:30:00.000-05:00', value=1))
        db.session.commit()

    def test_get_average_24h(self):
        averages = Average.getAverage24h()
        self.assertGreater(len(averages), 0) 
        self.assertIn('equipment_id', averages[0])  
        
    def test_get_average_48h(self):
        averages = Average.getAverage48h()
        self.assertGreater(len(averages), 0) 
        self.assertIn('equipment_id', averages[0])  
        
    def test_get_average_7d(self):
        averages = Average.getAverage7d()
        self.assertGreater(len(averages), 0) 
        self.assertIn('equipment_id', averages[0])  
    
    def test_get_average_30d(self):
        averages = Average.getAverage30d()
        self.assertGreater(len(averages), 0) 
        self.assertIn('equipment_id', averages[0])              
        