from flask import Blueprint, request

from ..db import SocmedDb

socmed = Blueprint('socmed', __name__, url_prefix='/socmed')

from .add import add
from .remove import remove


@socmed.route('/', methods=['GET'])
def get():
    user_id = request.args['user_id']

    socmed_db = SocmedDb()
    return socmed_db.find(user_id=user_id)
