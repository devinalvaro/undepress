from datetime import datetime
from flask import request
from flask_login import current_user, login_required

from . import userdata
from ..db import ChatDb


@userdata.route('/send', methods=['POST'])
@login_required
def send():
    sender_id = current_user.user_id
    receiver_id = int(request.form['receiver_id'])
    message = request.form['message']
    timestamp = datetime.utcnow()

    chat_db = ChatDb()
    chat_db.push(
        dict(sender_id=sender_id, receiver_id=receiver_id),
        messages=dict(message=message, timestamp=timestamp))

    return "CHAT_SEND_SUCCESS"
