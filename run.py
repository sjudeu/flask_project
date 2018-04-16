from mdblog.app import flask_app
from mdblog.app import init_db

import sys

def start():
    debug = True
    host = "0.0.0.0"
    flask_app.run(host, debug=debug)

def init():
    init_db(flask_app)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        commad = sys.argv[1]
        if commad == "start":
            start()
        elif commad == "init":
            init()
    else:
        print("usage:\n\n\trun.py [ start | init ]")
