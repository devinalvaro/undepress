from bson import json_util
from flask import Blueprint, current_app as app
from flask_login import login_required
from sklearn.externals import joblib

from ...lib.crawler import TwitterCrawler

detection = Blueprint('detection', __name__, url_prefix='/detection')


@detection.route('', methods=['GET'])
@login_required
def index():
    depression_detection = detect_depression(app)
    return json_util.dumps(depression_detection)


def detect_depression(app):
    twitter_crawler = TwitterCrawler(app)
    tweets = twitter_crawler.fetch_current_user_timeline()

    predictions = [
        detect_depression_symptoms(tweet['text']) for tweet in tweets
    ]
    return sum_predictions(predictions)


def detect_depression_symptoms(text):
    prediction = []
    for i in range(1, 10):
        classifier = joblib.load('data/classifier_' + str(i) + '.pkl')
        prediction.extend(classifier.predict([text]))
    return prediction


def sum_predictions(predictions):
    predictions_sum = [0 for _ in range(9)]
    for prediction in predictions:
        if int(prediction[0]):
            predictions_sum = [
                a + int(b) for a, b in zip(predictions_sum, prediction)
            ]
    return predictions_sum
