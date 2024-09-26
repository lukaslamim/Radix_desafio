import requests

def ValidBody(body):

    if 'username' not in body  or 'password' not in body:
        return False
    return True

def adminToken():
    url = 'http://127.0.0.1:5000/login'  
    admin_data = {
        'username': 'admin',
        'password': 'admin'
    }
    response = requests.post(url, json=admin_data)
    
    if response.status_code == 200:
        token = response.json().get('token')
        print("Token:", token)
        return
    else:
        print("Failed to authenticate admin. Response:", response.json())
        return