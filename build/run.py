#!/usr/bin/env python3
import json
import numpy as np
import requests
class ModelRequest:
  @staticmethod
  def diabetes(x):
    '''
    Pregnancies= int(1)
    Glucose= int(89)
    BloodPressure= int(66)
    SkinThickness= int(23)
    Insulin= int(94)
    BMI= float(28.1)
    DiabetesPedigreeFunction= float(0.167)
    Age= int(21)
    '''
    body = {"Pregnancies": x[0], "Glucose": x[1], "BloodPressure": x[2], 
        "SkinThickness": x[3], "Insulin": x[4], "BMI": x[5], 
        "DiabetesPedigreeFunction": x[6],
        "Age": x[7]}
    print(body)
    response = requests.post("http://127.0.0.1:5000/predict/Diabetes", data=body)
    if response.status_code == 500:
      return "internal server error"
    if response.status_code == 404:
      return "not found"
    if response.status_code == 400:
      return "bad request"
    if response.status_code == 200:
      return response.json()

x = ModelRequest()
a=[1, 89, 66, 23, 94, 28.1, 0.167, 21]
print(x.diabetes(a))


