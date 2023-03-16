#!/usr/bin/env python3
from flask_restful import reqparse
from flask_restful import Resource
import pickle
import numpy as np

model = pickle.load(open("model/heart.pkl", "rb"))

class Heart(Resource):
  @staticmethod
  def post():
    parser = reqparse.RequestParser()
    parser.add_argument("age")
    parser.add_argument("sex")
    parser.add_argument("cp")
    parser.add_argument("trestbps")
    parser.add_argument("chol")
    parser.add_argument("fbs")
    parser.add_argument("restecg")
    parser.add_argument("thalach")
    parser.add_argument("exang")
    parser.add_argument("oldpeak")
    parser.add_argument("slope")
    parser.add_argument("ca")
    parser.add_argument("thal")
    
    args = parser.parse_args()
    x = [np.fromiter(args.values() , dtype=float)]
    print(x)
    result = (model.predict(x))
    print(result)
    out = {"prediction" : int(result[0])}
    print(out)
    return out, 200
 

