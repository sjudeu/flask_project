from flask import Flask
from flask import render_template

from .models import db
from .mod_main import main
from .mod_blog import blog
from .mod_admin import admin

from .mod_main.forms import NewsletterForm

from mdblog import celery
from mdblog.celery_utils import make_celery

import os

def create_flask_app():
    flask_app = Flask(__name__)

    flask_app.config.from_pyfile("/vagrant/configs/default.py")
    if "MDBLOG_CONFIG" in os.environ:
        flask_app.config.from_envvar("MDBLOG_CONFIG")

    ## DB INIT
    db.init_app(flask_app)

    ## BLUEPRINTS
    flask_app.register_blueprint(main)
    flask_app.register_blueprint(blog)
    flask_app.register_blueprint(admin, url_prefix="/admin")

    ## INIT CELERY
    celery_app = make_celery(celery, flask_app)

    ## ERROR HANDLING
    @flask_app.errorhandler(500)
    def internal_server_error(error):
        return render_template("errors/500.jinja"), 500
    
    @flask_app.errorhandler(404)
    def internal_server_error(error):
        return render_template("errors/404.jinja"), 404
    
    ## FLASK CONTEXT PROCESSOR
    @flask_app.context_processor
    def inject_newsletter_form():
        return dict(newsletter_form = NewsletterForm())

    return flask_app, celery_app

