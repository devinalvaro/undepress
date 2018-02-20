from os import urandom


class Config:
    ADMIN_ID = 1
    SECRET_KEY = urandom(24)

    @staticmethod
    def init_app(app):
        pass
