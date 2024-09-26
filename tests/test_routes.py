import unittest
from app import createApp
from app.models.SensorUserModel import sensor_user
from app.models.SensorDataModel import sensor_data
from app.DataBase import db
import datetime

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = createApp()
        self.app.testing = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all() 
        self.client = self.app.test_client()

        self.client.post('/register', json={
            'username': 'tester',
            'password': 'tester'
        })

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login_user(self):
        response = self.client.post('/login', json={
            'username': 'tester',
            'password': 'tester'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json)

    def test_refresh_token(self):
        login_response = self.client.post('/login', json={
            'username': 'tester',
            'password': 'tester'
        })
        token = login_response.json['token']

        response = self.client.post('/refresh', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json)

    def test_average_sensor_data(self):
        for i in range(5):
            db.session.add(sensor_data(equipment_id=f'EQ-{i}', timestamp='2023-0112T01:30:00.000-05:00', value=1))
        db.session.commit()
        db.session.commit()

        response = self.client.get('/sensor/data/average')
        self.assertEqual(response.status_code, 200)
