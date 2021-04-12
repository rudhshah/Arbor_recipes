import flask
import ArborRecipe
from ArborRecipe.api.invalid_usage import InvalidUsage
from flask import jsonify



@ArborRecipe.app.route('/api/', methods=["GET"])
def get_urls():
  
    return flask.jsonify(ingredients="/api/i/", url="/api/")
