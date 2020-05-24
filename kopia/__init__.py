"""
kopia
===========

Root of entire project include app factory (create_app).
"""

from flask import Flask

from . import tag_filter
from . import ctx_processor
from . import database

from .views import main, moderator, admin, error


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.config['PATH'].mkdir(parents=True, exist_ok=True)

    database.init_app(app)

    load_views(app)
    load_template_filter(app)
    load_context_processor(app)
    load_error_page(app)

    return app


def load_views(app):
    app.register_blueprint(main.blueprint)
    app.add_url_rule('/', endpoint='home')

    app.register_blueprint(moderator.blueprint)
    app.register_blueprint(admin.blueprint)


def load_template_filter(app):
    app.add_template_filter(tag_filter.to_text)


def load_context_processor(app):
    app.context_processor(ctx_processor.processor)


def load_error_page(app):
    app.register_error_handler(404, error.page_not_found)
    app.register_error_handler(500, error.server_error)
