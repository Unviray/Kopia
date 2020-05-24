"""
kopia.views.main.request
========================

Request page.
"""

from datetime import date
from hashlib import sha1
from time import time

from flask import request, session

from tinydb import Query

from ...utils import templated, login_required
from ...database import get_db


@templated('user/request.html')
@login_required
def entry():
    db = get_db('request')
    q = Query()

    h = str(time())

    if request.method == 'POST':
        db.insert({
            "from": session['userId'],
            "date": date.today(),
            "req_id": sha1(h.encode()).hexdigest(),
            "reason": request.form['reason'],
        })

    req_list = db.search(q['from'] == session['userId'])

    return {'req_list': req_list}
