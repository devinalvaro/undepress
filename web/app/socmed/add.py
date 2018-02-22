from flask import request
from flask_login import login_required

from . import socmed
from ..db import SocmedDb


@socmed.route('/add', methods=['POST'])
@login_required
def add():
    form_data = get_form_data(request)

    socmed_db = SocmedDb()
    if socmed_db.find_one(user_id=form_data['user_id']):
        socmed_db.set(
            dict(user_id=form_data['user_id']),
            twitter=form_data['twitter'],
            facebook=form_data['facebook'],
            instagram=form_data['instagram'])
    else:
        socmed_db.insert(**form_data)

    return "SOCMED_ADD_SUCCESS"


def get_form_data(request):
    return dict(
        user_id=int(request.form['user_id']),
        twitter=request.form.get('twitter'),
        facebook=request.form.get('facebook'),
        instagram=request.form.get('instagram'))
