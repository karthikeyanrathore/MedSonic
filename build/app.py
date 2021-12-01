#!/usr/bin/env python3
from flask import Flask, render_template
from flask import request
app = Flask(__name__)
from run import ModelRequest

@app.route("/")
def home():
  return "Hello World"


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






if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=5001)
