from flask import jsonify, make_response
import unittest

def createResponse(content, status):
    
    return  make_response(
        jsonify(
        content
        )
        , status
    )  

def run_tests():
    loader = unittest.TestLoader()
    tests = loader.discover('tests')  
    test_runner = unittest.TextTestRunner()
    test_runner.run(tests)    