from os import urandom


class Config:
    ADMIN_ID = 1
    SECRET_KEY = urandom(24)
    TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN') or 'you-will-never-guess'
	TWITTER_ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_SECRET') or 'you-will-never-guess'
	TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY') or 'you-will-never-guess'
	TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET') or 'you-will-never-guess'
	
    @staticmethod
    def init_app(app):
        pass
