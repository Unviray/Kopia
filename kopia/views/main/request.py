"""
kopia.views.main.request
========================

Request page.
"""

from ...utils import templated, login_required


@templated('user/request.html')
@login_required
def entry():
    return {}
