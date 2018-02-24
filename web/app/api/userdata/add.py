from flask import request
from flask_login import login_required

from . import userdata
from ...db import UserdataDb


@userdata.route('/add', methods=['POST'])
@login_required
def add():
    form_data = get_form_data(request)
    insert_userdata(form_data)

    return "USERDATA_ADD_SUCCESS"


def get_form_data(request):
    return dict(
        user_id=int(request.form['user_id']),
        data_type=request.form['data_type'],
        data=request.form['data'],
        timestamp=request.form['timestamp'])


def insert_userdata(form_data):
    UserdataDb.insert(**form_data)
