from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import g

import sqlite3
import os


flask_app = Flask(__name__)

flask_app.config.from_pyfile("/vagrant/configs/default.py")

if "MDBLOG_CONFIG" in os.environ:
    flask_app.config.from_envvar("MDBLOG_CONFIG")

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja")

@flask_app.route("/about/")
def view_about():
    return render_template("about.jinja")

@flask_app.route("/admin/")
def view_admin():
    if "logged" not in session:
        return redirect(url_for("view_login"))
    return render_template("admin.jinja")

@flask_app.route("/articles/", methods=["GET"])
def view_articles():
    db = get_db()
    cur = db.execute("select * from articles order by id desc")
    articles = cur.fetchall()
    return render_template("articles.jinja", articles=articles)

@flask_app.route("/articles/", methods=["POST"])
def add_article():
    db = get_db()
    db.execute("insert into articles (title, content) values (?, ?)",
            [request.form.get("title"), request.form.get("content")])
    db.commit()
    return redirect(url_for("view_articles"))

@flask_app.route("/articles/<int:art_id>/")
def view_article(art_id):
    db = get_db()
    cur = db.execute("select * from articles where id=(?)",[art_id])
    article = cur.fetchone()
    if article:
        return render_template("article.jinja", article=article)
    return render_template("article_not_found.jinja", art_id=art_id)

@flask_app.route("/login/", methods=["GET"])
def view_login():
    return render_template("login.jinja")

@flask_app.route("/login/", methods=["POST"])
def login_user():
    username = request.form["username"]
    password = request.form["password"]
    if username == flask_app.config["USERNAME"] and \
            password == flask_app.config["PASSWORD"]:
        session["logged"] = True
        return redirect(url_for("view_admin"))
    else:
        return redirect(url_for("view_login"))

@flask_app.route("/logout/", methods=["POST"])
def logout_user():
    session.pop("logged")
    return redirect(url_for("view_welcome_page"))


## UTILS
def connect_db():
    rv = sqlite3.connect(flask_app.config["DATABASE"])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@flask_app.teardown_appcontext
def close_db(error):
    if hasattr(g, "sqlite_db"):
        g.sqlite_db.close()

def init_db(app):
    with app.app_context():
        db = get_db()
        with open("mdblog/schema.sql", "r") as fp:
            db.cursor().executescript(fp.read())
        db.commit()
