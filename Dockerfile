FROM python:3.6

COPY requirements.txt /mdblog/requirements.txt
RUN pip install -r /mdblog/requirements.txt


COPY ./mdblog /mdblog

COPY ./configs/docker.py /mdblog/docker.py
COPY ./configs/uwsgi/docker_wsgi.ini /mdblog/docker_wsgi.ini

EXPOSE 80

ENV MDBLOG_CONFIG=/mdblog/docker.py

CMD ["uwsgi", "--ini", "/mdblog/docker_wsgi.ini"]
