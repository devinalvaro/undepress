from flask import Blueprint

account = Blueprint('account', __name__, url_prefix='/account')

from .login import login
from .register import register
from .logout import logout

from .user import User
