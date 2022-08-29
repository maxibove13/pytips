#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Module with minimal flask-restx app"""

from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

# Routes are defined by classes
@api.route('/hello')
class HelloWorld(Resource):
    # The HTTP petitions are method of each route class
    def get(self):
        return {'hello': 'world'}

@api.route('/goodbye')
class GoodBye(Resource):
    def post(self):
        name = api.payload['name']
        return {'Responding to a POST petition containing the name': name}

if __name__ == "__main__":
    app.run(debug=True, port=5000)