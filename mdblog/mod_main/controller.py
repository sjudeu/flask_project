from flask import Blueprint
from flask import render_template

main = Blueprint("main", __name__)


@main.route("/")
def view_welcome_page():
    return render_template("mod_main/welcome_page.jinja")

@main.route("/about/")
def view_about():
    return render_template("mod_main/about.jinja")

