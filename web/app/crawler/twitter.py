from bson import json_util
from flask import current_user, request

from . import crawler
from .twitter_api import TwitterAPI
from ..db import SocmedDb


@crawler.route('/twitter/fetch', methods=['POST'])
def fetch():
    form_data = get_form_data(request)
    twitter_api = TwitterAPI()
    return json_util.dumps(
        twitter_api.fetch_user_timeline(form_data['username']))


def get_form_data(request):
    user_id = current_user.user_id
    username = SocmedDb.find_one(user_id=user_id)['twitter']
    return dict(username=username)
