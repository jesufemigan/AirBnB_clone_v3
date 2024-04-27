#!/usr/bin/python3
"""a flask web app"""

from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from models import storage
from os import getenv


HOST = getenv('HBNB_API_HOST') if getenv('HBNB_API_HOST') else '0.0.0.0'
PORT = getenv('HBNB_API_PORT') if getenv('HBNB_API_PORT') else 5000

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(exc):
    """closes the database session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Error page Not found"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, threaded=True)
