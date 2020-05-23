"""
kopia.views.main.login
======================

User login page.
"""

from flask import (
    session,
    redirect,
    url_for as url
)

from ...utils import templated
from ...forms import UserLoginForm


@templated('user/login.html')
def entry():
    user_login_handler = UserLoginHandler(UserLoginForm)

    pushed = user_login_handler.push()

    if pushed:
        return redirect(url('main.request'))

    return {
        'form': user_login_handler.form,
    }


class UserLoginHandler(object):
    """
    Handler for User Login Form
    """

    def __init__(self, form_class):
        self.form_class = form_class
        self.form = form_class()

    def push(self):
        if self.form.validate_on_submit():
            session['userId'] = self.form.ID.data
            return True
        else:
            return False
