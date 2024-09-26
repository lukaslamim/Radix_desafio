from locust import HttpUser, between, task
import json

class SensorDataUser(HttpUser):
    wait_time = between(1, 2)  # Tempo de espera entre as requisições

    @task
    def insert_sensor_data(self):
        payload = {
            "equipmentId": "EQ-teste",
            "timestamp": "2023-01-12T01:30:00.000-05:00",
            "value": 25.5
        }
        self.client.post("/sensor/data", data=json.dumps(payload), headers={"Content-Type": "application/json"})

        return
# Para rodar o teste, utilize o seguinte comando:
# locust -f payload_test.py --host=http://127.0.0.1:5000