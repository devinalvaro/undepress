from flask import Blueprint, current_app as app, request

from .twitter_api import TwitterAPI

crawler = Blueprint('crawler', __name__, url_prefix='/crawler')

from .twitter import fetch
