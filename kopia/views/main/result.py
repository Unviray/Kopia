"""
kopia.views.main.request
========================

Request page.
"""
from werkzeug.exceptions import abort

from tinydb import Query

from ...utils import templated
from ...database import get_db


@templated('user/result.html')
def entry(req_id):
    rdb = get_db('request')
    db = get_db()
    q = Query()
    page = rdb.get(q.req_id == req_id)

    if page is None:
        abort(404)

    user = db.get(q.ID == page['from'])

    return {'page': page, 'user': user}
