"""
kopia.views.moderator
=====================

Handle views for moderator.
Many view here accept POST method for search in navbar or other POST.
"""

from flask import Blueprint

from . import request_list, login


blueprint = Blueprint('moderator', __name__, url_prefix='/moderator')


blueprint.add_url_rule(
    '/',
    'login',
    login.entry,
    methods=['GET', 'POST'])

blueprint.add_url_rule(
    '/lisitra-fangatahana',
    'request_list',
    request_list.entry,
    methods=['GET', 'POST'])
