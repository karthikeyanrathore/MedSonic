#!/usr/bin/env python3
class Model:
  def get():
    import tensorflow as tf
    # load json and create model
    f = open('model/model.json', 'r')
    savemodel= f.read()
    model= tf.keras.models.model_from_json(savemodel)
    model.summary()

    # load weights
    from keras.models import load_model
    model.load_weights('model/model.h5')
    model.compile(loss='sparse_categorical_crossentropy', optimizer='SGD', metrics=['accuracy'])
    return model

  def resize(path):
    import  skimage 
    from skimage import filters
    import cv2
    img = cv2.imread(path)
    return skimage.transform.resize(img, (200, 200, 3))
    
  def predict(path):
    model = Model.get()
    img = Model.resize(path)
    return model.predict(img)
   

x = Model.predict("data/person1946_bacteria_4874.jpeg")
