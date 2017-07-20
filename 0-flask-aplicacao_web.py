#!flask/bin/python
from flask import Flask

aplicacao_web = Flask(__name__)

@aplicacao_web.route('/')
def index():
    return "Ola Mundo!"

if __name__ == '__main__':
    aplicacao_web.run(debug=True)
