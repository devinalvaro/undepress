from flask import request
from flask_login import current_user, login_required

from . import socmed
from ...lib.db import SocmedDb


@socmed.route('/set', methods=['POST'])
@login_required
def set():
    form_data = get_form_data(request)
    set_socialmedia(form_data)

    return "SOCMED_SET_SUCCESS", 204


def get_form_data(request):
    return dict(
        twitter=request.form.get('twitter'),
        facebook=request.form.get('facebook'),
        instagram=request.form.get('instagram'))


def set_socialmedia(form_data):
    SocmedDb.set(dict(user_id=current_user.user_id), **form_data)
