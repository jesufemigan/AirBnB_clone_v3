#!/usr/bin/python3
""" Create a new view for Place object that handles all default RESTFul API actions"""
from models import Place, Reviews
from models import storage
from flask import abort, jsonify, make_response, require
from api.view.v1.views import app_views


@app_views.route('/places/reviews', methods=['GET'], strict_slashes = False)
def get_reviews(place_id):
    """ Retrieves the list of all Review objects of a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = Place.reviews
    list = []
    for rev in reviews:
        list.append(rev.to_dict())
    return jsonify(list)
    
@app_views.route('/reviews', methods=['GET'], strict_slashes = False)
def get_review(review_id):
    """ Retrieves a Review object """
    rev = storage.get(Review, review_id)
    if rev is None:
        abort(404)
    return jsonify(rev.to_dict())

@app_views.route('/reviews', methods=['DELETE'], strict_slashes = False)
def del_review(review_id):
    """ Deletes Review objecs """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/reviews', methods=['POST'], strict_slashes = False)
def post_review(place_id):
    """ Creates a Review """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if not request.get_json():
        abort(404, Not a JSON)
    if 'user_id' not in request.get_json():
        abort(404, Missing user_id)
    if 'text' not in request.get_json():
        abort(404, Missing text)
     input = request.get_json()
    user = storage.get(User, input['user_id'])
    if user is None:
        abort(404)
    ins = Review(**input)
    ins.place_id = place_id
    ins.save()
    return make_response(jsonify(ins.to_dict()), 201)

@app_views.route('/reviews', methods=['PUT'], strict_slashes = False)
def put_review(review_id):
    """ Updates a Review object """
    rev = storage.get(Review, review_id)
    if rev is None:
        abort(404)
    if not request.get_json():
        abort(404, Not a JSON)
    ignore = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
    input = request.get_json()
    for k, v in input.items():
        if k not in ignore:
            setattr(rev, k, v)
    storage.save()
    return make_response(jsonify(rev.to_dict), 200)
