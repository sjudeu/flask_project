from mdblog.app import flask_app

if __name__ == "__main__":
    debug = True
    host = "0.0.0.0"
    flask_app.run(host, debug=debug)
