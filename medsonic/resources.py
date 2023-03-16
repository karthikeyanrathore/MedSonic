from flask_restful import Resource
from flask import make_response, jsonify

class DsStatus(Resource):
    # Diabetes model status checker
    def get(self):
        # TODO: check if diabetes model is uptodate.
        return make_response(jsonify({"status": "OK"}), 200)


class PnStatus(Resource):
    # Pneumonia model status checker
    def get(self):
        # TODO: check if pneumonia model is uptodate.
        return make_response(jsonify({"status": "OK"}), 200)


class HeartStatus(Resource):
    # HeartModel status checker
    def get(self):
        # TODO: check if heart model is uptodate.
        return make_response(jsonify({"status": "OK"}), 200)
