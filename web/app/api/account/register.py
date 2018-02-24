from flask import render_template, request

from . import account
from ...lib.db import AccountDb


@account.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    form_data = get_form_data(request)
    if does_email_exist(form_data):
        return "ACCOUNT_REGISTER_EXIST"
    else:
        register_account(form_data)

        return "ACCOUNT_REGISTER_SUCCESS"


def get_form_data(request):
    return dict(
        email=request.form['email'],
        password=request.form['password'],
        name=request.form['name'],
        address=request.form['address'],
        phone=request.form['phone'],
        is_expert=bool(request.form.get('email')))


def does_email_exist(form_data):
    return AccountDb.find_one(email=form_data['email'])


def register_account(form_data):
    # TODO: salt password
    AccountDb.insert(**form_data)
