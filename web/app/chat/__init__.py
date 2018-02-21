from bson import json_util
from flask import Blueprint, request
from flask_login import current_user

from ..db import ChatDb

chat = Blueprint('chat', __name__, url_prefix='/chat')

from .send import send


@chat.route('/', methods=['GET'])
def index():
    sender_id = int(request.args['sender_id'])
    receiver_id = current_user.user_id

    chat_db = ChatDb()
    return json_util.dumps(
        chat_db.find(sender_id=sender_id, receiver_id=receiver_id))

    return "CHAT_SEND_SUCCESS"
