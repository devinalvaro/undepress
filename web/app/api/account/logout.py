from flask_login import login_required, logout_user

from . import account


@account.route('/logout')
@login_required
def logout():
    logout_user()

    return "ACCOUNT_LOGOUT_SUCCESS"
