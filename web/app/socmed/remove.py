from flask import request
from flask_login import login_required

from . import socmed
from ..db import SocmedDb


@socmed.route('/remove', methods=['POST'])
@login_required
def remove():
    form_data = get_form_data(request)
    if does_document_exist(form_data):
        unset_socialmedia(form_data)

        return "SOCMED_REMOVE_SUCCESS"
    else:
        return "SOCMED_REMOVE_UNEXIST"


def get_form_data(request):
    return dict(
        user_id=int(request.form['user_id']),
        twitter=request.form.get('twitter'),
        facebook=request.form.get('facebook'),
        instagram=request.form.get('instagram'))


def does_document_exist(form_data):
    return SocmedDb.find_one(user_id=form_data['user_id'])


def unset_socialmedia(form_data):
    SocmedDb.unset(
        dict(user_id=form_data['user_id']),
        twitter=form_data['twitter'],
        facebook=form_data['facebook'],
        instagram=form_data['instagram'])
