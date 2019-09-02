'''
함수의 docstring입니다.
'''
from flask import Flask
APP = Flask(__name__)

@APP.route('/')
def hello_world():
    '''
    함수의 docstring입니다.
    '''
    return 'Hello, World!'
