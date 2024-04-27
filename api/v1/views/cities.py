#!/usr/bin/python3
""" objects that handle RESTFUL actions for Cities """

from models import City
from Flask import abort, jsonify, make_respnse, request
from api.v1.views import app_views
from models import storage


@app_view.route('/states/<states_id>/cities', methods=['GET'], stirct_slashes=False)
def all_city(states_id):
    """ Retrieves the list of all City objects of a State"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    list_cities = []
    for city in state.citites:
        list_cities.append(city.to_dict())
    return jsonify(list_cities)

@app_view.route('/cities/<cities_id>', methdos=['GET'], strict_slashes=False)
def get_city(city_id):
    """ Gets a City object """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict)

@app_view.route('/cities', methods=['DELETE'], strict_slashes=False)
def del_city(city_id):
    """ Deletes a City object """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return make_response(jsonify({}), 200)

@app_view.route('/states/<states_id>/cities', methods=['POST'], strict_slashes=False)
    def add_city(state_id):
        state = storage.get(State, state_id)
        if state is None:
            abort(404)
        if not request.get_json():
            abort(404, Not a JSON)
        if 'name' not in request.get_json():
            abort(404, Missing name)
        input = request.get_json()
        ins = City(**input)
        ins.state_id = state.id
        storage.save()
        return make_response(jsonify(ins.to_dict(), 201)

@app_view.route('/cities', methods=['POST'], strict_slashes=False)
def update_city(city_id):
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.get_json():
        abort(404, Not a JSON)
    input = response.get_json()
    ignore = ['id', 'state_id', 'created_at', 'updated_at']
    for k, v in input.items():
        if k not in ignore:
            setattr(city, k, v)
    storage.save()
    return make_response(jsonify(city.to_dict()), 200)
