from flask import request
from flask_login import login_required

from . import userdata
from ..db import UserdataDb


@userdata.route('/add', methods=['POST'])
@login_required
def add():
    user_id = int(request.form['user_id'])
    data_type = request.form['data_type']
    data = request.form['data']
    timestamp = request.form['timestamp']

    userdata_db = UserdataDb()
    userdata_db.insert(
        user_id=user_id, data_type=data_type, data=data, timestamp=timestamp)

    return "USERDATA_ADD_SUCCESS"
