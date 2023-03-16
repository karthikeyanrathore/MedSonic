from flask import Blueprint
from flask_restful import Api

from medsonic.resources import (
    DsStatus,
    PnStatus,
    HeartStatus,
    PnPredict,
    DsPredict,
    HeartPredict,
    MakeReport,
)

pneumonia_bp = Blueprint("pneumonia", __name__)
diabetes_bp = Blueprint("diabetes", __name__)
heart_bp = Blueprint("heart", __name__)
md_helper_bp = Blueprint("medsonic helper", __name__)

pneumonia_api = Api(pneumonia_bp)
diabetes_api = Api(diabetes_bp)
heart_api = Api(heart_bp)
md_helper_api = Api(md_helper_bp)

pneumonia_api.add_resource(PnStatus, "/")
# pneumonia_api.add_resource(PnPredict, "/predict")

diabetes_api.add_resource(DsStatus, "/")
# diabetes_api.add_resource(DsPredict, "/predict")

heart_api.add_resource(HeartStatus, "/")
heart_api.add_resource(HeartPredict, "/predict")

# md_helper_api.add_resource(MakeReport, "/report")