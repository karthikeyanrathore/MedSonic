#!/usr/bin/env python3
from flask import Flask
from flask_restful import Api
from diabetes import Diabetes
app = Flask(__name__)
API = Api(app)

API.add_resource(Diabetes, "/predict/Diabetes")

if __name__ == "__main__":
  app.run(debug=True)


