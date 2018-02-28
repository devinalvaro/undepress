from bson import json_util
from flask import Blueprint, request
from flask_login import current_user, login_required

from ...lib.db import ChatDb

chat = Blueprint('chat', __name__, url_prefix='/chat')

from .send import send


@chat.route('/', methods=['GET'])
@login_required
def index():
    form_data = get_form_data(request)
    return json_util.dumps(get_chat_data(form_data))


def get_form_data(request):
    return dict(
        our_id=current_user.user_id, their_id=int(request.args['their_id']))


def get_chat_data(form_data):
    query = {
        '$or': [
            dict(
                sender_id=form_data['our_id'],
                receiver_id=form_data['their_id']),
            dict(
                sender_id=form_data['their_id'],
                receiver_id=form_data['our_id'])
        ]
    }
    return sort_chats_by_timestamp(ChatDb.find(**query))


def sort_chats_by_timestamp(chats):
    return sorted(chats, key=lambda chat: chat['timestamp'])
