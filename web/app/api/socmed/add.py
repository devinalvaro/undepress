from flask import request
from flask_login import current_user, login_required

from . import socmed
from ...lib.db import SocmedDb


@socmed.route('/add', methods=['POST'])
@login_required
def add():
    form_data = get_form_data(request)
    if does_document_exist(form_data):
        set_socialmedia(form_data)
    else:
        insert_socialmedia(form_data)

    return "SOCMED_ADD_SUCCESS"


def get_form_data(request):
    return dict(
        user_id=current_user.user_id,
        twitter=request.form.get('twitter'),
        facebook=request.form.get('facebook'),
        instagram=request.form.get('instagram'))


def does_document_exist(form_data):
    return SocmedDb.find_one(user_id=form_data['user_id'])


def set_socialmedia(form_data):
    SocmedDb.set(
        dict(user_id=form_data['user_id']),
        twitter=form_data['twitter'],
        facebook=form_data['facebook'],
        instagram=form_data['instagram'])


def insert_socialmedia(form_data):
    SocmedDb.insert(**form_data)
