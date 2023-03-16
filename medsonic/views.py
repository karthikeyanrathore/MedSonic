from flask import Blueprint
from flask_restful import Api
from medsonic.resources import (
    DsStatus,
    PnStatus,
    HeartStatus,
)

pneumonia_bp = Blueprint("pneumonia", __name__)
diabetes_bp = Blueprint("diabetes", __name__)
heart_bp = Blueprint("heart", __name__)

pneumonia_api = Api(pneumonia_bp)
diabetes_api = Api(diabetes_bp)
heart_api = Api(heart_bp)

pneumonia_api.add_resource(PnStatus, "/")
diabetes_api.add_resource(DsStatus, "/")
heart_api.add_resource(HeartStatus, "/")