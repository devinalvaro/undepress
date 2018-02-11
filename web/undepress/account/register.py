from db import AccountDb


def register(email, password):
    account_db = AccountDb()

    if account_db.find(email, password):
        return "REGISTER_EXIST"
    else:
        account_db.insert(email, password)
        return "REGISTER_SUCCESS"
