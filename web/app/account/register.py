from flask import render_template, request

from . import account
from ..db import AccountDb


@account.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    form_data = get_form_data(request)

    account_db = AccountDb()
    if account_db.find_one(email=form_data['email']):
        return "ACCOUNT_REGISTER_EXIST"
    else:
        # TODO: salt password
        account_db.insert(**form_data)

        return "ACCOUNT_REGISTER_SUCCESS"


def get_form_data(request):
    return dict(
        email=request.form['email'],
        password=request.form['password'],
        name=request.form['name'],
        address=request.form['address'],
        phone=request.form['phone'],
        is_expert=bool(request.form.get('email')))
