from app.routes.SensorDataRoute import RegisterSensorDataRoutes
from app.routes.UserRoute import RegisterUserRoutes

def RouteRegistrer(app):

    RegisterSensorDataRoutes(app)
    RegisterUserRoutes(app)
    return