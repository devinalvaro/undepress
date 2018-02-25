from flask_login import current_user, login_required

from . import account
from ...lib.token import unset_token


@account.route('/logout')
@login_required
def logout():
    unset_token(current_user.user_id)

    return "ACCOUNT_LOGOUT_SUCCESS"
