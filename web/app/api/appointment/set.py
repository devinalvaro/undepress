from flask import request
from flask_login import current_user, login_required

from . import socmed
from ...lib.db import SocmedDb


@socmed.route('/set', methods=['POST'])
@login_required
def set():
    form_data = get_form_data(request)
    set_socialmedia(form_data)

    return "SOCMED_SET_SUCCESS"


def get_form_data(request):
    form_data = dict(
        patient_id=request.form.get('patient_id'),
        expert_id=request.form.get('expert_id'),
        status=request.form['status'])

    if not form_data['patient_id']:
        form_data['patient_id'] = current_user.user_id
    elif not form_data['expert_id']:
        form_data['expert_id'] = current_user.user_id


def set_socialmedia(form_data):
    SocmedDb.set(**form_data)
