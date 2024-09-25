from flask import jsonify, make_response

def createResponse(content, status):
    
    return  make_response(
        jsonify(
        content
        )
        , status
    )  