from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash

from mdblog.models import db
from mdblog.models import Article
from mdblog.models import User

from .forms import ArticleForm
from .forms import ChangePasswordForm
from .forms import LoginForm

from .utils import login_required


admin = Blueprint("admin", __name__)


@admin.route("/")
@login_required
def view_admin():
    page=request.args.get("page", 1, type=int)
    paginate = Article.query.order_by(Article.id.desc()).paginate(
            page, 10, False)
    return render_template("mod_admin/admin.jinja",
            articles=paginate.items,
            paginate=paginate)

@admin.route("/articles/new/", methods=["GET"])
@login_required
def view_add_article():
    form = ArticleForm()
    return render_template("mod_admin/article_editor.jinja", form=form)

@admin.route("/articles/", methods=["POST"])
@login_required
def add_article():
    add_form = ArticleForm(request.form)
    if add_form.validate():
        new_article = Article(
                title = add_form.title.data,
                content = add_form.content.data,
                html_render = add_form.html_render.data)
        db.session.add(new_article)
        db.session.commit()
        flash("Article was saved", "alert-success")
        return redirect(url_for("blog.view_articles"))
    else:
        for error in add_form.errors:
            flash("{} is required".format(error), "alert-danger")
        return render_template("mod_admin/article_editor.jinja", form=add_form)


@admin.route("/articles/<int:art_id>/edit/", methods=["GET"])
@login_required
def view_article_editor(art_id):
    article = Article.query.filter_by(id=art_id).first()
    if article:
        form = ArticleForm()
        form.title.data = article.title
        form.content.data = article.content
        return render_template("mod_admin/article_editor.jinja", form=form, article=article)
    return render_template("mod_blog/article_not_found.jinja", art_id=art_id)


@admin.route("/articles/<int:art_id>/", methods=["POST"])
@login_required
def edit_article(art_id):
    article = Article.query.filter_by(id=art_id).first()
    if article:
        edit_form = ArticleForm(request.form)
        if edit_form.validate():
            article.title = edit_form.title.data
            article.content = edit_form.content.data
            article.html_render = edit_form.html_render.data
            db.session.add(article)
            db.session.commit()
            flash("Edit saved", "alert-success")
            return redirect(url_for("blog.view_article", art_id=art_id))
        else:
            for error in login_form.errors:
                flash("{} is missing".format(error), "alert-danger")
            return redirect(url_for("admin.view_login"))

@admin.route("/login/", methods=["GET"])
def view_login():
    login_form = LoginForm()
    return render_template("mod_admin/login.jinja", form=login_form)

@admin.route("/login/", methods=["POST"])
def login_user():
    login_form = LoginForm(request.form)
    if login_form.validate():
        user = User.query.filter_by(username = login_form.username.data).first()
        if user and user.check_password(login_form.password.data):
            session["logged"] = user.username
            flash("Login successful", "alert-success")
            return redirect(url_for("admin.view_admin"))
        else:
            flash("Invalid credentials", "alert-danger")
            return render_template("mod_admin/login.jinja", form=login_form)
    else:
        for error in login_form.errors:
            flash("{} is missing".format(error), "alert-danger")
        return redirect(url_for("admin.view_login"))

@admin.route("/changepassword/", methods=["GET"])
@login_required
def view_change_password():
    form = ChangePasswordForm()
    return render_template("mod_admin/change_password.jinja", form=form)

@admin.route("/changepassword/", methods=["POST"])
@login_required
def change_password():
    form = ChangePasswordForm(request.form)
    if form.validate():
        user = User.query.filter_by(username = session["logged"]).first()
        if user and user.check_password(form.old_password.data):
            user.set_password(form.new_password.data)
            db.session.add(user)
            db.session.commit()
            flash("Password changed!", "alert-success")
            return redirect(url_for("admin.view_admin"))
        else:
            flash("Invalid credentials", "alert-danger")
            return render_template("mod_admin/change_password.jinja", form=form)
    else:
        for error in form.errors:
            flash("{} is missing".format(error), "alert-danger")
        return render_template("mod_admin/change_password.jinja", form=form)

@admin.route("/logout/", methods=["POST"])
@login_required
def logout_user():
    session.pop("logged")
    flash("Logout successful", "alert-success")
    return redirect(url_for("main.view_welcome_page"))
