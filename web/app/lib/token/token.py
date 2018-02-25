from ...lib.db import TokenDb


# TODO: generate better token
def generate_token(request, user_id):
    return "TOKEN:" + str(user_id)


# TODO: parse more informations
def parse_token(token):
    dump, user_id = token.split(':')
    return dict(user_id=int(user_id))


def is_token_valid(user_id, token):
    return TokenDb.find_one(user_id=user_id, token=token)


def set_token(user_id, token):
    TokenDb.set(dict(user_id=user_id), token=token)


def unset_token(user_id):
    TokenDb.unset(dict(user_id=user_id), token=1)
