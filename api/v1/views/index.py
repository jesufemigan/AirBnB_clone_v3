#!/usr/bin/python3
"""define route /status"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def api_status():
    """displays status of api"""
    return jsonify({"status": "OK"})
