#!/usr/bin/python3
'''index.py'''
from api.v1.views import app_views
from flask import jsonify
import models
from models import amenity, city, place, review, state, user


@app_views.route('/status', strict_slashes=False)
def status():
    """return status"""
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/stats', strict_slashes=False)
def some_stats():
    """return stats"""
    dict = {
        "amenities": models.storage.count("Amenity"),
        "cities": models.storage.count("City"),
        "places": models.storage.count("Place"),
        "reviews": models.storage.count("Review"),
        "states": models.storage.count("State"),
        "users": models.storage.count("User")
    }
    return dict
