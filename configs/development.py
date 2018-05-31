import os

DEBUG = True
# DATABASE = "/vagrant/blog.db"
SQLALCHEMY_DATABASE_URI = "sqlite:////vagrant/blog.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
CELERY_BROKER_URL="pyamqp://guest@localhost//"

# NEWSLETTER EMAIL ACCOUNT
EMAIL_USERNAME=os.environ.get("MDBLOG_EMAIL_USERNAME", None)
EMAIL_PASSWORD=os.environ.get("MDBLOG_EMAIL_PASSWORD", None)
