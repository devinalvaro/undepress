from datetime import datetime
from flask import request
from flask_login import current_user, login_required

from . import chat
from ...lib.db import ChatDb


@chat.route('/send', methods=['POST'])
@login_required
def send():
    form_data = get_form_data(request)
    push_chat(form_data)

    return "CHAT_SEND_SUCCESS", 201


def get_form_data(request):
    return dict(
        sender_id=current_user.user_id,
        receiver_id=int(request.form['receiver_id']),
        message=request.form['message'],
        timestamp=str(datetime.now()))


def push_chat(form_data):
    ChatDb.insert(**form_data)
