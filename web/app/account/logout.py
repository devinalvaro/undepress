from flask_login import login_required, logout_user

from . import account

@account.route('/account/logout')
@login_required
def logout():
    logout_user()
    return "LOGOUT_SUCCESS"
