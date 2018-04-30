from flask import current_app as app
from jwt import decode, encode

from ...lib.db import TokenDb


def encode_token(user_id):
    return encode(
        dict(user_id=user_id), app.config['SECRET_KEY'],
        algorithm='HS256').decode('utf-8')


def decode_token(token):
    return decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])


def is_token_valid(user_id, token):
    return TokenDb.find_one(user_id=user_id, token=token) is not None


def set_token(user_id, token):
    TokenDb.set(dict(user_id=user_id), token=token)


def unset_token(user_id):
    TokenDb.unset(dict(user_id=user_id), token=1)
