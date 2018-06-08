import os

SECRET_KEY = b'""\x9ac\xbc\x82\xcb\xd0\xa7\xe8Y\xecsV/\x93F\xeax\x99\xa3\x7f\x03\t'
DEBUG=False
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False

EMAIL_USERNAME=os.environ.get("MDBLOG_EMAIL_USERNAME", None)
EMAIL_PASSWORD=os.environ.get("MDBLOG_EMAIL_PASSWORD", None)

## CELERY CONFIG
BROKER_URL = os.environ.get("CLOUDAMQP_URL")

BROKER_POOL_LIMIT = 1
BROKER_HEARTBEAT = None
BROKER_CONNECTION_TIMEOUT = 30
CELERY_RESULT_BACKEND = None
EVENT_QUEUE_EXPIRES = 60
WORKER_PREFETCH_MULTIPLIER = 1
WORKER_CONCURRENCY = 50
