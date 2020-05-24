"""
kopia.views.admin.login
======================

Admin login page.
"""

from flask import request, redirect, url_for as url

from ...utils import templated


@templated('admin/login.html')
def entry():
    if request.method == 'POST':
        if request.form['username'] == request.form['password'] == 'admin':
            return redirect(url('admin.home'))

    return {}
