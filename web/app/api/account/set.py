from flask import request
from flask_login import current_user, login_required

from . import account
from ...lib.db import AccountDb


@account.route('/set', methods=['POST'])
@login_required
def set():
    form_data = get_form_data(request)
    set_account(form_data)

    return "ACCOUNT_SET_SUCCESS"


def get_form_data(request):
    return dict(
        email=request.form.get('email'),
        password=request.form.get('password'),
        name=request.form.get('name'),
        address=request.form.get('address'),
        phone=request.form.get('phone'),
        is_expert=bool(request.form.get('is_expert')),
        is_expert_verified=bool(request.form.get('is_expert_verified')),
        expert_description=request.form.get('expert_description'),
        expert_experience=request.form.get('expert_experience'),
        expert_location=request.form.get('expert_location'))


def set_account(form_data):
    AccountDb.set(dict(user_id=current_user.user_id), **form_data)
