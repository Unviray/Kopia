"""
kopia.ctx_processor
==================

Context processor (function used in template).
"""

from werkzeug.utils import import_string

from flask import (
    url_for as url,
    current_app as app, )


def processor():
    def get_widget(name, *args, **kwargs):
        path_module = f'kopia.views.widgets.{name}:entry'
        module_widget = import_string(path_module)

        return module_widget(*args, **kwargs)

    return dict(
        len=len,
        str=str,
        round=round,
        url=url,  # use url insted of url_for (it's too long)
        app=app,  # access app in template
        widget=get_widget, )
