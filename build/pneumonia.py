#!/usr/bin/env python3
class Model:
  def get():
    from keras.models import load_model
    # load json and create model
    model = load_model("model/pneumonia_model.h5")
    model.summary()
    return model

  def resize(path):
    import  skimage 
    from skimage import filters
    import cv2
    import numpy as np
    img = cv2.imread(path)
    img = skimage.transform.resize(img, (200, 200, 3))
    return np.expand_dims(img, axis=0)
    
  def predict(path):
    model = Model.get()
    img = Model.resize(path)
    result = model.predict(img)
    # good-luck
    if result[[0]] > 0.6:
      return 1
    else:
      return 0

   
