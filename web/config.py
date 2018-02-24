from os import environ


class Config:
    ADMIN_ID = int(environ.get('ADMIN_ID'))
    SECRET_KEY = environ.get('SECRET_KEY')
    TWITTER_ACCESS_TOKEN = environ.get('TWITTER_ACCESS_TOKEN')
    TWITTER_ACCESS_SECRET = environ.get('TWITTER_ACCESS_SECRET')
    TWITTER_CONSUMER_KEY = environ.get('TWITTER_CONSUMER_KEY')
    TWITTER_CONSUMER_SECRET = environ.get('TWITTER_CONSUMER_SECRET')

    @staticmethod
    def init_app(app):
        pass
