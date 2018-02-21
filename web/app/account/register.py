from flask import render_template, request

from . import account
from ..db import AccountDb


@account.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    email = request.form['email']
    password = request.form['password']
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']
    is_expert = bool(request.form.get('is_expert'))

    account_db = AccountDb()
    if account_db.find_one(email=email):
        return "ACCOUNT_REGISTER_EXIST"
    else:
        # TODO: salt password
        account_db.insert(
            email=email,
            password=password,
            name=name,
            address=address,
            phone=phone,
            is_expert=is_expert)

        return "ACCOUNT_REGISTER_SUCCESS"
