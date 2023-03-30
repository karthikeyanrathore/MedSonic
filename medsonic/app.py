from medsonic.views import (
    diabetes_bp,
    pneumonia_bp,
    heart_bp,
    md_helper_bp,
)
from medsonic import config
from flask import Flask, make_response, jsonify
from flask_cors import CORS


def endpoint_not_found(e):
    return make_response(
        jsonify({"error": "The requested URL was not found on the server."}), 404)


def handle_assertion_error(e):
    return make_response(jsonify({"AssertionError": (e.__str__())}), 404)

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = config.DEBUG

    if config.CORS:
        print("CORS running on flask-app")
        CORS(app)

    # custom error handler
    # https://flask.palletsprojects.com/en/2.2.x/errorhandling/
    app.register_error_handler(404, endpoint_not_found)
    app.register_error_handler(AssertionError, handle_assertion_error)

    app.register_blueprint(
        diabetes_bp, url_prefix=f"/{config.CURRENT_VERSION_API}/diabetes"
    )
    app.register_blueprint(
        pneumonia_bp, url_prefix=f"/{config.CURRENT_VERSION_API}/pneumonia"
    )
    app.register_blueprint(heart_bp, url_prefix=f"/{config.CURRENT_VERSION_API}/heart")
    app.register_blueprint(
        md_helper_bp, url_prefix=f"/{config.CURRENT_VERSION_API}/medsonic/helper"
    )
    return app
