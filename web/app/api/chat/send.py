from flask import request
from flask_login import current_user, login_required

from . import chat
from ...lib.db import ChatDb


@chat.route('/send', methods=['POST'])
@login_required
def send():
    form_data = get_form_data(request)
    push_chat(form_data)

    return "CHAT_SEND_SUCCESS"


def get_form_data(request):
    return dict(
        sender_id=current_user.user_id,
        receiver_id=int(request.form['receiver_id']),
        message=request.form['message'],
        timestamp=request.form['timestamp'])


def push_chat(form_data):
    query = dict(
        sender_id=form_data['sender_id'], receiver_id=form_data['receiver_id'])
    message = dict(
        message=form_data['message'], timestamp=form_data['timestamp'])
    ChatDb.push(query, messages=message)
