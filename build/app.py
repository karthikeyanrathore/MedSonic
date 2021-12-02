#!/usr/bin/env python3
import os
from flask import Flask, render_template
from flask import request
app = Flask(__name__)
from run import ModelRequest
from pneumonia import Model
UPLOAD_FOLDER = 'store/images'

@app.route("/")
def home():
  #return "Hello World"
  return render_template("index.html")

@app.route("/heart", methods=['GET', 'POST'])
def heart():
  features = [float(x) for x in request.form.values()]
  print(features)
  x = ModelRequest
  result = x.heart(features)
  if result is not None:
    if result['prediction']:
      result = "YES"
    else:
      result = "NO"
  return render_template("heart.html", result=result)

@app.route("/diabetes", methods=['GET', 'POST'])
def diabetes():
  features = [float(x) for x in request.form.values()]
  print(features)
  x = ModelRequest
  result = x.diabetes(features)
  if result is not None:
    if result['prediction']:
      result = "YES"
    else:
      result = "NO"
  return render_template("diabetes.html", result=result)


@app.route("/pneumonia", methods=['GET', 'POST'])
def pneumonia():
  result = None
  if request.method == "POST":
    image = request.files['img']
    path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(path)
    result = Model.predict(path)
    if result:
      result = "YES"
    else:
      result = "NO"
  return render_template("pneumonia.html", result=result) 


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=5001)
