from bson import json_util
from flask import Blueprint, request
from flask_login import current_user, login_required

from ..db import ChatDb

chat = Blueprint('chat', __name__, url_prefix='/chat')

from .send import send


@chat.route('/', methods=['GET'])
@login_required
def index():
    form_data = get_form_data(request)

    chat_db = ChatDb()
    return json_util.dumps(
        chat_db.find(**form_data))

    return "CHAT_SEND_SUCCESS"


def get_form_data(request):
    return dict(
        sender_id=int(request.args['sender_id']),
        receiver_id=current_user.user_id)
