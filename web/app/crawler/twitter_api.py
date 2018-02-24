from flask_login import current_user
from twitter import Twitter, OAuth

from ..db import SocmedDb


class TwitterAPI:
    def __init__(self, app):
        self.__ACCESS_TOKEN = app.config['TWITTER_ACCESS_TOKEN']
        self.__ACCESS_SECRET = app.config['TWITTER_ACCESS_SECRET']
        self.__CONSUMER_KEY = app.config['TWITTER_CONSUMER_KEY']
        self.__CONSUMER_SECRET = app.config['TWITTER_CONSUMER_SECRET']
        self.__oauth = OAuth(self.__ACCESS_TOKEN, self.__ACCESS_SECRET,
                             self.__CONSUMER_KEY, self.__CONSUMER_SECRET)
        self.__twitter = Twitter(auth=self.__oauth)

    def fetch_current_user_timeline(self):
        user_id = current_user.user_id
        username = SocmedDb.find_one(user_id=user_id)['twitter']
        return self.fetch_user_timeline(username)

    def fetch_user_timeline(self, username):
        return self.__twitter.statuses.user_timeline(screen_name=username)
