#!/usr/bin/python3
""" a view for State objects that handle all Restful Actions"""

from models.state import State
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request

@app_views('/states', methods=['GET'], strict_slashes=False)

def get_states():
    """ Retrieves the list of all State objects """"
    state_all = storage.all(State).values()
    list_all = []
    for state in state_all:
        list_all.append(state.to_dict())
    return(jsonify(list_all))

@app_views('/states', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """ Retrieves a State object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return(jsonify(state.to_dict))

@app_views('/states', methods=['DELETE'], strict_slashes=False)
def del_state(state_id):
    """ Deletes an object of State """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return (make_response(jsonify({}), 200))

@app_views('/states', method=['POST'], strict_slashes=False)
del new_state():
    """ Creates a State"""
    if not request.get_json:
        abort(404, Not a JSON)
    if 'name' not in request.get_json:
        abort(404, Missing name)
    input = request.get_json
    instance = State(**input)
    return (make_response(jsonify(instance), 201))

@app_views('/states', methods=['PUT'], strict_slashes=False)
del update(state_id):
    """Updates a State object"""
    state = storage.get(State, state_id)
    if state id None:
        abort(404)
    if not request.get_json:
        abort(404, Not a JSON)
    ignore = ['id', 'created_at', 'updated_at']
    for k, v in state.items():
        if k not in ignore:
            state[k] = v
    storage.save()
    return make_response(jsonify(state.to_dict()), 200)