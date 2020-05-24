"""
kopia.views.admin
=====================

Handle views for admin.
Many view here accept POST method for search in navbar or other POST.
"""

from flask import Blueprint

from . import login, home


blueprint = Blueprint('admin', __name__, url_prefix='/admin')


blueprint.add_url_rule(
    '/',
    'login',
    login.entry,
    methods=['GET', 'POST'])

blueprint.add_url_rule(
    '/fandraisana',
    'home',
    home.entry,
    methods=['GET', 'POST'])
