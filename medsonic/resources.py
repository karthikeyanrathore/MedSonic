from flask_restful import Resource
from flask import make_response, jsonify, request
import numpy as np
import pickle 
import os
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
        pass

class PnPredict(Resource):
    # Make pneumonia prediction and log it.
    def post(self):
        pass

class HeartPredict(Resource):
    # Make heart disease prediction and log it.
    def post(self):
        payload = request.get_json()
        if not payload:
            return make_response(
                jsonify({"error": "Bad Request"}), 400
            )
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
        model_input = [np.fromiter(payload.values() , dtype=float)]
        try:
            # features should be in same order as training model. check notebook
            # TODO: make dynamic feature input.
            result = imported_model.predict(model_input)
        except ValueError as error:
            msg = "error.%s" % repr(error)
            return make_response(
                jsonify({"error": msg}, 200)
        )
        return make_response(
            jsonify({"prediction": bool(result[0])}, 200)
        )


class MakeReport(Resource):
    # Make .csv report w.r.t disease.
    def get(self):
        pass