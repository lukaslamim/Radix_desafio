python -m venv venv
pip install -r requirements.txt

#para rodar localmente necessario alterar o parametro em app\__init__.py
#de
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lukas:741852@db:5432/sensor_database'
#para
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lukas:741852@localhost:5432/sensor_database'