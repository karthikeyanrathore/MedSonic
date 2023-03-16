#!/usr/bin/env python3
from flask_restful import reqparse
from flask_restful import Resource
import pickle
import numpy as np

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
    x = [float(args.Pregnancies), float(args.Glucose), float(args.BloodPressure), float(args.SkinThickness), float(args.Insulin), float(args.BMI), float(args.DiabetesPedigreeFunction), float(args.Age)]
    
    maxy = np.array([ 17.  , 199.  , 122.  ,  99.  , 846.  ,  67.1 ,   2.42,  81.  ])
    miny = np.array([ 0.   ,  0.   ,  0.   ,  0.   ,  0.   ,  0.   ,  0.078, 21.   ])
    
    for i in range(0, len(x)):
      x[i] = (x[i] - miny[i])/(maxy[i] - miny[i])
    
    x = np.array(x)
    x = x.reshape((1, 8))
    result = (model.predict(x))
    print(result)
    out = {"prediction" : int(result[0])}
    print(out)
    return out, 200
 

