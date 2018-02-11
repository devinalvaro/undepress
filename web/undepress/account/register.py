from db import AccountDb


def register(email,
             password,
             name,
             address,
             phone,
             is_expert=False,
             experience=None):
    account_db = AccountDb()

    if account_db.find_one(email=email):
        return "REGISTER_EXIST"
    else:
        account_db.insert(
            email=email,
            password=password,
            name=name,
            address=address,
            phone=phone,
            is_expert=is_expert,
            experience=experience,
        )
        return "REGISTER_SUCCESS"
