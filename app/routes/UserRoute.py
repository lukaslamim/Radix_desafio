from flask import request, make_response
from app.DataBase import db
from flask_bcrypt import Bcrypt
from app.models.SensorUserModel import sensor_user
from app.services import SensorUserService
import datetime, jwt 

bcrypt = Bcrypt()

def RegisterUserRoutes(app):
    #InsertUser
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        if SensorUserService.ValidBody(data):
            hashed_password = bcrypt.generate_password_hash(password=data['password']).decode('utf-8')
            new_user = sensor_user(username=data['username'], password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return make_response({'message': 'User created'}, 201)
        else:
            return make_response({"Error": "Invalid request, 'username' and/or 'password' not found in request."}, 400)
        
    #getBearerToken
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        if SensorUserService.ValidBody(data):
            user = sensor_user.query.filter_by(username=data['username']).first()
            if bcrypt.check_password_hash(user.password, password=data['password']):
                token = jwt.encode({
                    'user_id': user.id,
                    'exp': datetime.datetime.now() + datetime.timedelta(hours=24)
                }, app.config['SECRET_KEY'], algorithm='HS256')
                return make_response({'token': token}, 200)
            return make_response({'message': 'Invalid credentials'}, 401)
        else:
            return make_response({"Error": "Invalid request, 'username' and/or 'password' not found in request."}, 400)

    @app.route('/refresh', methods=['POST'])
    def refresh():
        old_token = request.headers.get('Authorization').split()[1]
        try:
            payload = jwt.decode(old_token, app.config['SECRET_KEY'], algorithms=['HS256'])
            new_token = jwt.encode({
                'user_id': payload['user_id'],
                'exp': datetime.datetime.now() + datetime.timedelta(hours=24)
            }, app.config['SECRET_KEY'], algorithm='HS256')
            return {'token': new_token}, 200
        except Exception as e:
            return make_response({'Error': str(e)}, 401)
    
    #validateBearerToken
    @app.route('/protected', methods=['GET'])
    def protected():
        token = request.headers.get('Authorization').split()[1]
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            user = sensor_user.query.get(data['user_id'])
            return make_response({'message': f'Welcome {user.username}'}, 200)
        except Exception as e:
            return make_response({'Error': str(e)}, 401)