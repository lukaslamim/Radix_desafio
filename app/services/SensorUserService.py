def ValidBody(body):

    if 'username' not in body  or 'password' not in body:
        return False
    return True
