from flask_restful import Resource
from flask import make_response, jsonify, request
# from keras.models import load_model
import numpy as np
import pickle
import os
import tempfile
from medsonic.config import MEDSONIC_REPO_DIR


class DsStatus(Resource):
    # Diabetes model status checker
    def get(self):
        # TODO: check if default diabetes model is uptodate.
        return make_response(jsonify({"status": "OK"}), 200)


class PnStatus(Resource):
    # Pneumonia model status checker
    def get(self):
        # TODO: check if default pneumonia model is uptodate.
        return make_response(jsonify({"status": "OK"}), 200)


class HeartStatus(Resource):
    # HeartModel status checker
    def get(self):
        # TODO: check if default heart model is uptodate.
        return make_response(jsonify({"status": "OK"}), 200)


class DsPredict(Resource):
    # Make diabetes prediction and log it.
    # Add option for custom model.
    def post(self):
        payload = request.get_json()
        if not payload:
            return make_response(jsonify({"error": "Bad Request"}), 400)
        # Todo: idk validate payload (not necessary)
        dfmodel_path = f"{MEDSONIC_REPO_DIR}/medsonic/default_models/diabetes_model.pkl"
        if not os.path.exists(dfmodel_path):
            # for docker container: /home/medsonic
            dfmodel_path = f"{MEDSONIC_REPO_DIR}/default_models/diabetes_model.pkl"
        if not os.path.exists(dfmodel_path):
            return make_response(
                jsonify({"error": "Model not found in the server."}), 404
            )
        imported_model = pickle.load(open(dfmodel_path, "rb"))
        model_input = [np.fromiter(payload.values(), dtype=float)]

        # Hard coded stuff: dk why?
        maxy = np.array([ 17.  , 199.  , 122.  ,  99.  , 846.  ,  67.1 ,   2.42,  81.  ])
        miny = np.array([ 0.   ,  0.   ,  0.   ,  0.   ,  0.   ,  0.   ,  0.078, 21.   ])
        for i in range(0, len(model_input)):
            model_input[i] = (model_input[i] - miny[i])/(maxy[i] - miny[i])

        model_input = np.array(model_input)
        try:
            assert model_input.size == 8, "Warning: Numpy array size is not 8"
            model_input = model_input.reshape((1, 8))
            # features should be in same order as training model. check notebook
            # TODO: make dynamic feature input.
            result = imported_model.predict(model_input)
        except ValueError as error:
            msg = "error.%s" % repr(error)
            return make_response(jsonify({"error": msg}), 200)
        return make_response(jsonify({"prediction": bool(result[0])}), 200)
        

class PnPredict(Resource):
    # Make pneumonia prediction and log it.
    def post(self):
        # TODO: Think ways of adding tensorflow to docker.
        # pip install tensorflow (530 mb) will take forever.

        # if request.content_type.find("multipart/form-data") < 0:
        #     return make_response(jsonify({"error": "Bad content type. Accepted Request: multipart format."}), 400)
        # _payload = request.form.to_dict()
        # image_file = request.files["image"]

        # dfmodel_path = f"{MEDSONIC_REPO_DIR}/medsonic/default_models/heart_model.pkl"
        # if not os.path.exists(dfmodel_path):
        #     # for docker container: /home/medsonic
        #     dfmodel_path = f"{MEDSONIC_REPO_DIR}/default_models/heart_model.pkl"
        # if not os.path.exists(dfmodel_path):
        #     return make_response(
        #         jsonify({"error": "Model not found in the server."}), 404
        #     )
        # imported_model = load_model(dfmodel_path)
        # imported_model.summary()

        # with tempfile.TemporaryDirectory() as ftd:
        #     image_path = os.path.join(ftd, image_file.filename)
        #     image_file.save(image_path)

        # return "NotImplemented"
        pass


class HeartPredict(Resource):
    # Make heart disease prediction and log it.
    def post(self):
        payload = request.get_json()
        if not payload:
            return make_response(jsonify({"error": "Bad Request"}), 400)
        # Todo: idk validate payload (not necessary)
        dfmodel_path = f"{MEDSONIC_REPO_DIR}/medsonic/default_models/heart_model.pkl"
        if not os.path.exists(dfmodel_path):
            # for docker container: /home/medsonic
            dfmodel_path = f"{MEDSONIC_REPO_DIR}/default_models/heart_model.pkl"
        if not os.path.exists(dfmodel_path):
            return make_response(
                jsonify({"error": "Model not found in the server."}), 404
            )
        imported_model = pickle.load(open(dfmodel_path, "rb"))
        model_input = [np.fromiter(payload.values(), dtype=float)]
        try:
            assert model_input.size == 13, "Warning: Numpy array size is not 13"
            # features should be in same order as training model. check notebook
            # TODO: make dynamic feature input.
            result = imported_model.predict(model_input)
        except ValueError as error:
            msg = "error.%s" % repr(error)
            return make_response(jsonify({"error": msg}), 200)
        return make_response(jsonify({"prediction": bool(result[0])}), 200)


class MakeReport(Resource):
    # Make .csv report w.r.t disease.
    def get(self):
        pass
