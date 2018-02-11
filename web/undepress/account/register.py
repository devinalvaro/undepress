from db import AccountDb


def register(email, password):
    account_db = AccountDb()

    if account_db.find(email, password):
        return "Account already exists"
    else:
        account_db.insert(email, password)
        return "Register successful"
