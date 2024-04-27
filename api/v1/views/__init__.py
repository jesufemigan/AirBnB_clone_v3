#!/usr/bin/python3
"""view for app v1"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.view.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
