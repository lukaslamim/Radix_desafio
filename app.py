from app import createApp
from app.services import SensorUserService
import threading

app = createApp()

def run_admin_test():
    SensorUserService.adminToken()

threading.Thread(target=run_admin_test).start()

app.run()

