from twitter import Twitter, OAuth


class TwitterAPI:
    def __init__(self, app):
        self.__ACCESS_TOKEN = app.config['TWITTER_ACCESS_TOKEN']
        self.__ACCESS_SECRET = app.config['TWITTER_ACCESS_SECRET']
        self.__CONSUMER_KEY = app.config['TWITTER_CONSUMER_KEY']
        self.__CONSUMER_SECRET = app.config['TWITTER_CONSUMER_SECRET']
        self.__oauth = OAuth(self.__ACCESS_TOKEN, self.__ACCESS_SECRET,
                             self.__CONSUMER_KEY, self.__CONSUMER_SECRET)
        self.__twitter = Twitter(auth=self.__oauth)

    def fetch_user_timeline(self, username):
        return self.__twitter.statuses.user_timeline(screen_name=username)
