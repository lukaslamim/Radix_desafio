

def listToJson(List):
    return [sensor.toJson() for sensor in List]


def ValidBody(body):
    
    if (not body or 'equipment_id' not in body or 'value' not in body
            or not body['equipment_id'].startswith("EQ-")):
        return False
    try:
        float(body['value'])
    except ValueError:
        return False
    
    return True
           