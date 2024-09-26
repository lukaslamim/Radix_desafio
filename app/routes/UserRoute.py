from flask import request, make_response
from app.DataBase import db
from flask_bcrypt import Bcrypt
from app.models.UserModel import User
import datetime, jwt 


def RegisterUserRoutes(app):
    #InsertUser
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        hashed_password = Bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_user = User(username=data['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return make_response({'message': 'User created'}, 201)

    #AuthUser
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and Bcrypt.check_password_hash(user.password, data['password']):
            token = jwt.encode({
                'user_id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, app.config['SECRET_KEY'], algorithm='HS256')
            return make_response({'token': token}, 200)
        return make_response({'message': 'Invalid credentials'}, 401)

    #getAuthorization
    @app.route('/protected', methods=['GET'])
    def protected():
        token = request.headers.get('Authorization').split()[1]
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            user = User.query.get(data['user_id'])
            return make_response({'message': f'Welcome {user.username}'}, 200)
        except:
            return make_response({'message': 'Token is invalid!'}, 401)