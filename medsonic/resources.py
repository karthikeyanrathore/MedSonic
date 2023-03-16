from flask_restful import Resource
from flask import make_response, jsonify

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
        pass

class MakeReport(Resource):
    # Make .csv report w.r.t disease.
    def get(self):
        pass