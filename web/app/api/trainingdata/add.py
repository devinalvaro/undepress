from flask import request
from flask_login import login_required

from . import trainingdata
from ...lib.db import TrainingdataDb


@trainingdata.route('/add', methods=['POST'])
@login_required
def add():
    form_data = get_form_data(request)
    insert_trainingdata(form_data)

    return "TRAININGDATA_ADD_SUCCESS"


def get_form_data(request):
    return dict(
        label=request.form['label'],
        symptoms=[request.form.get('symptom_' + i) for i in range(1, 10)])


def insert_trainingdata(form_data):
    TrainingdataDb.insert(**form_data)
