#!/usr/bin/python3
'''app.py'''
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', '5000')

app = Flask(__name__)


@app.teardown_appcontext
def teardown_app(exception):
    """close storage"""
    storage.close()


@app.errorhandeler(404)
def error_404(error):
    """return 404"""
    return {"error": "Not found"}, 404


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
