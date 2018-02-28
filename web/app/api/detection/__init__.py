from bson import json_util
from flask import Blueprint, current_app as app
from flask_login import login_required
from sklearn.externals import joblib

from ...lib.crawler import TwitterCrawler

detection = Blueprint('detection', __name__, url_prefix='/detection')


@detection.route('', methods=['GET'])
@login_required
def index():
    return json_util.dumps(get_depression_detection(app))


def get_depression_detection(app):
    twitter_crawler = TwitterCrawler(app)
    tweets = twitter_crawler.fetch_current_user_timeline()

    predictions = [
        detect_depression_symptoms([tweet['text']]) for tweet in tweets
    ]
    return predictions


def detect_depression_symptoms(text):
    prediction = []
    for i in range(1, 10):
        classifier = joblib.load('data/classifier_' + str(i) + '.pkl')
        prediction.extend(classifier.predict(text))
    return prediction
