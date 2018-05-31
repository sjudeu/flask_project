from mdblog import celery
from mdblog.models import Newsletter
from time import sleep

from celery.utils.log import get_task_logger

from email.message import EmailMessage
import smtplib

from flask import current_app

logger = get_task_logger(__name__)

@celery.task
def notify_newsletter(url):
    subscribers = Newsletter.query.all()
    logger.info("number of subscribers: {:03d}".format(len(subscribers)))
    for subscriber in subscribers:
        logger.info("sending email to {}".format(subscriber.email))
        username = current_app.config.get("EMAIL_USERNAME")
        password = current_app.config.get("EMAIL_PASSWORD")
        send_email(username, password,
                subscriber.email, url)

def send_email(user, passwd, to_email, url):
    from_email = user # používame svoj mail na prihlásenie

    mail = EmailMessage()
    mail.set_content("new blog at {url}".format(url=url))

    mail["Subject"] = "New blog!"
    mail["From"] = from_email
    mail["To"] = to_email

    try:  
        # inicializácia spojenia -> gmail vyžaduje ssl
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()

        # login
        server_ssl.login(user, passwd)

        # poslanie mailu
        server_ssl.send_message(mail, from_email, to_email)

        # ukoncenie spojenia
        server_ssl.close()
        logger.info("mail send!")
    except Exception as e:  
        logger.error('nieco sa pokazilo')
        logger.error(e)
