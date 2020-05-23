"""
kopia.views.main
===============

Handle main first views.
Many view here accept POST method for search in navbar or other POST.
"""

from flask import Blueprint

from . import request, login


blueprint = Blueprint('main', __name__)


blueprint.add_url_rule(
    '/',
    'login',
    login.entry,
    methods=['GET', 'POST'])

blueprint.add_url_rule(
    '/fangatahana',
    'request',
    request.entry,
    methods=['GET', 'POST'])
