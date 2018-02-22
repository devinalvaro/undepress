from datetime import datetime
from flask import request
from flask_login import current_user, login_required

from . import chat
from ..db import ChatDb


@chat.route('/send', methods=['POST'])
@login_required
def send():
    form_data = get_form_data(request)

    chat_db = ChatDb()
    if not chat_db.find_one(
            sender_id=form_data['sender_id'],
            receiver_id=form_data['receiver_id']):
        chat_db.insert(
            sender_id=form_data['sender_id'],
            receiver_id=form_data['receiver_id'])
    chat_db.push(
        dict(
            sender_id=form_data['sender_id'],
            receiver_id=form_data['receiver_id']),
        messages=dict(
            message=form_data['message'], timestamp=form_data['timestamp']))

    return "CHAT_SEND_SUCCESS"


def get_form_data(request):
    return dict(
        sender_id=current_user.user_id,
        receiver_id=int(request.form['receiver_id']),
        message=request.form['message'],
        timestamp=datetime.utcnow())
