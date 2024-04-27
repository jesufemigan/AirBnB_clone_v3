#!/usr/bin/python3
""" Create a new view for Place object that handles all default RESTFul API actions"""
from models import Place, City, State
from models import storage
from flask import abort, jsonify, make_response, require
from api.view.v1.views import app_views


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes = False)
def get_places(city_id):
    """ Retrieves the list of all Places objects of a City"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    places = City.places
    list = []
    for place in places:
        list.append(place.to_dict())
    return jsonify(list)
    
@app_views.route('/places', methods=['GET'], strict_slashes = False)
def get_places(places_id):
    """ Retrieves a Places object """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())

@app_views.route('/places', methods=['DELETE'], strict_slashes = False)
def del_place(place_id):
    """ Deletes Place objecs """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes = False)
def post_place(city_id):
    """ Creates a Place """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.get_json():
        abort(404, Not a JSON)
    if 'user_id' not in request.get_json():
        abort(404, Missing user_id)
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if 'name' not in request.get_json():
        abort(404, Missing name)
    input = request.get_json()
    ins = Place(**input)
    ins.city_id = city_id
    ins.save()
    return make_response(jsonify(ins.to_dict()), 201)

@app_views.route('/places', methods=['PUT'], strict_slashes = False)
def put_place(place_id):
    """ Updates a Place object """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if not request.get_json():
        abort(404, Not a JSON)
    ignore = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
    input = request.get_json()
    for k, v in input.items():
        if k not in ignore:
            setattr(place, k, v)
    storage.save()
    return make_response(jsonify(place.to_dict()), 200)