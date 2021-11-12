#!/usr/bin/env python3
from flask import Flask
from flask_restful import Api
from diabetes import Diabetes
from heart import Heart 
app = Flask(__name__)
API = Api(app)

API.add_resource(Diabetes, "/predict/Diabetes")
API.add_resource(Heart, "/predict/Heart")

if __name__ == "__main__":
  app.run(debug=True)


