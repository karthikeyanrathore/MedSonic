#!/usr/bin/env python3
import json
import numpy as np
import requests
class ModelRequest:
  @staticmethod
  def diabetes(x):
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
  
  @staticmethod
  def heart(x):
    body = { "age": x[0], "sex": x[1], "cp": x[2], "trestbps": x[3], "chol": x[4],
        "fbs": x[5], "restecg": x[6], "thalach": x[7], "exang": x[8], "oldpeak": x[9],
        "slope": x[10], "ca": x[11], "thal": x[12]}
    print(body)
    response = requests.post("http://127.0.0.1:5000/predict/Heart", data=body)
    if response.status_code == 500:
      return "internal server error"
    if response.status_code == 404:
      return "not found"
    if response.status_code == 400:
      return "bad request"
    if response.status_code == 200:
      return response.json()



x = ModelRequest()
#a=[1, 89, 66, 23, 94, 28.1, 0.167, 21]
#print(x.diabetes(a))

#a=[63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]
a=[43, 0, 0, 132, 341, 1, 0, 136, 1, 3, 1, 0, 3]
print(x.heart(a))






