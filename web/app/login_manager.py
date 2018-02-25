from flask_login import LoginManager

from .lib.user import User
from .lib.token import is_token_valid, decode_token

login_manager = LoginManager()


@login_manager.request_loader
def load_user(request):
    token = request.headers.get('Authorization')
    if token:
        decoded_token = decode_token(token)
        user_id = decoded_token['user_id']
        if is_token_valid(user_id, token):
            return User(user_id)
    else:
        return None
