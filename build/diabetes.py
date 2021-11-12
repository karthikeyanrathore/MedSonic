#!/usr/bin/env python3
from flask import Flask
from flask_restful import Api
from flask_restful import reqparse
from flask_restful import Resource
import pickle
import numpy as np

app = Flask(__name__)
API = Api(app)
model = pickle.load(open("model/diabetes.pkl", "rb"))

class Diabetes(Resource):
  @staticmethod
  def post():
    parser = reqparse.RequestParser()
    parser.add_argument("Pregnancies")
    parser.add_argument("Glucose")
    parser.add_argument("BloodPressure")
    parser.add_argument("SkinThickness")
    parser.add_argument("Insulin")
    parser.add_argument("BMI")
    parser.add_argument("DiabetesPedigreeFunction")
    parser.add_argument("Age")
    args = parser.parse_args()
    x = [np.fromiter(args.values() , dtype=float)]
    print(x)
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    x = scaler.fit_transform(x)

    result = (model.predict(x))
    print(result)
    out = {"prediction" : int(result[0])}
    print(out)
    return out, 200
 

API.add_resource(Diabetes, "/predict/Diabetes")

if __name__ == "__main__":
  app.run(debug=True)


