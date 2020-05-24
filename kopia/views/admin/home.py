from flask import request

from tinydb import Query

from ...database import get_db
from ...utils import templated


@templated('admin/home.html')
def entry():
    db = get_db()
    rdb = get_db('request')
    mdb = get_db('moderator')

    if request.method == 'POST':
        if request.form['pointing'] == 'user':
            db.insert({
                'ID': request.form['id'],
                'full_name': request.form['name'],
                'birth_date': request.form['b_date'],
                'birth_place': request.form['b_place'],
                'commune': request.form['commune'],
                'gender': request.form['gender'],
            })

    return locals()
