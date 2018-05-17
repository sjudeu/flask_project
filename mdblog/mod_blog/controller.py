from flask import Blueprint
from flask import render_template
from flask import request

from mdblog.models import Article

blog = Blueprint("blog", __name__)


@blog.route("/articles/", methods=["GET"])
def view_articles():
    page = request.args.get("page", 1, type=int)
    paginate = Article.query.order_by(Article.id.desc()).paginate(page, 5, False)
    return render_template("mod_blog/articles.jinja",
            articles=paginate.items,
            paginate=paginate)

@blog.route("/articles/<int:art_id>/")
def view_article(art_id):
    article = Article.query.filter_by(id=art_id).first()
    if article:
        return render_template("mod_blog/article.jinja", article=article)
    return render_template("mod_blog/article_not_found.jinja", art_id=art_id)
