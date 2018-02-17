from flask import render_template, request

from . import account
from ..db import AccountDb


@account.route('/account/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        address = request.form['address']
        phone = request.form['phone']
        is_expert = False  # TODO: fix is_expert

        account_db = AccountDb()

        if account_db.find_one(email=email):
            return "REGISTER_EXIST"
        else:
            account_db.insert(
                email=email,
                password=password,
                name=name,
                address=address,
                phone=phone,
                is_expert=is_expert,
                experience=None,
            )
            return "REGISTER_SUCCESS"
