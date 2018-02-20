from flask import request

from . import socmed
from ..db import SocmedDb


@socmed.route('/add', methods=['POST'])
def add():
    user_id = request.form['user_id']
    twitter = request.form.get('twitter')
    facebook = request.form.get('facebook')
    instagram = request.form.get('instagram')

    socmed_db = SocmedDb()
    if socmed_db.find(user_id=user_id):
        socmed_db.set(
            dict(user_id=user_id),
            twitter=twitter,
            facebook=facebook,
            instagram=instagram)
    else:
        socmed_db.insert(
            user_id=user_id,
            twitter=twitter,
            facebook=facebook,
            instagram=instagram)

    return "SOCMED_INSERT_SUCCESS"
