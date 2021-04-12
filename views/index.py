import flask
from flask import request
import ArborRecipe

@ArborRecipe.app.route('/', methods=['GET', 'POST'])
def show_index():
    """Index page."""
    context = {"hi": "hi"}
    return flask.render_template("index.html", **context)