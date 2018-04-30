from flask import request
from flask_login import current_user, login_required

from . import account
from ...lib.db import AccountDb
from ...lib.password import hash_password


@account.route('/set', methods=['POST'])
@login_required
def set():
    form_data = get_form_data(request)
    set_account(form_data)

    return "ACCOUNT_SET_SUCCESS", 204


def get_form_data(request):
    return dict(
        email=request.form.get('email'),
        password=ensure_hashed(request.form.get('password')),
        name=request.form.get('name'),
        address=request.form.get('address'),
        phone=request.form.get('phone'),
        is_expert=ensure_boolean(request.form.get('is_expert')),
        is_expert_verified=ensure_boolean(
            request.form.get('is_expert_verified')),
        expert_description=request.form.get('expert_description'),
        expert_experience=request.form.get('expert_experience'),
        expert_location=request.form.get('expert_location'),
        expert_picture=request.form.get('expert_picture'))


def set_account(form_data):
    AccountDb.set(dict(user_id=current_user.user_id), **form_data)


def ensure_hashed(password):
    return hash_password(password) if password is not None else None


def ensure_boolean(boolean):
    return bool(boolean) if boolean is not None else None
