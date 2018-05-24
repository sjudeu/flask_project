from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from .forms import NewsletterForm

from mdblog.models import Newsletter
from mdblog.models import db

main = Blueprint("main", __name__)


@main.route("/")
def view_welcome_page():
    return render_template("mod_main/welcome_page.jinja")

@main.route("/about/")
def view_about():
    return render_template("mod_main/about.jinja")

@main.route("/newsletter/", methods=["POST"])
def add_newsletter():
    newsletter_form = NewsletterForm(request.form)
    if newsletter_form.validate():
        newsletter = Newsletter(email=newsletter_form.email.data)
        db.session.add(newsletter)
        db.session.commit()
        flash("You were successfully subscribed", "alert-success")
    else:
        for error in newsletter_form.errors:
            flash("{} is not valid".format(error), "alert-danger")
    return redirect(url_for("main.view_welcome_page"))

