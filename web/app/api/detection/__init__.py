from bson import json_util
from flask import Blueprint, current_app as app
from flask_login import login_required
from sklearn.externals import joblib

from ...lib.crawler import TwitterCrawler
from ...lib.nlp import preprocess

detection = Blueprint('detection', __name__, url_prefix='/detection')


@detection.route('', methods=['GET'])
@login_required
def index():
    depression_detection = detect_depression(app)

    if depression_detection is not None:
        return json_util.dumps(depression_detection)
    else:
        return "DETECTION_USERNAME_NOT_FOUND"


def detect_depression(app):
    twitter_crawler = TwitterCrawler(app)
    tweets = twitter_crawler.fetch_current_user_timeline()

    if tweets is not None:
        predictions = [
            detect_depression_symptoms(preprocess(tweet['text']))
            for tweet in tweets
        ]
        predictions_sum = sum_predictions(predictions)
        predictions_sum_total = sum_predictions(predictions, include_all=True)
        return classify_prediction(predictions_sum, predictions_sum_total)


def detect_depression_symptoms(text):
    prediction = []
    for i in range(1, 10):
        classifier = joblib.load('data/classifier_' + str(i) + '.pkl')
        prediction.extend(classifier.predict([text]))
    return prediction


def sum_predictions(predictions, include_all=False):
    predictions_sum = [0 for _ in range(9)]
    for prediction in predictions:
        if include_all or int(prediction[0]):
            predictions_sum = [
                a + int(b) for a, b in zip(predictions_sum, prediction)
            ]
    return predictions_sum


def classify_prediction(predictions_sum, predictions_sum_total):
    return [
        1 if a / b >= 0.5 else 0
        for a, b in zip(predictions_sum, predictions_sum_total)
    ]
