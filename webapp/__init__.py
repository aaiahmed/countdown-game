from flask import Flask, redirect, url_for
from flask_session import Session
from . import countdown


def create_app():
    app = Flask(__name__)
    app.secret_key = "my super secret key"
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    app.config['CACHE_TYPE'] = 'simple'

    @app.route('/')
    def count_down():
        return redirect(url_for('countdown'))

    app.register_blueprint(countdown.bp)
    app.add_url_rule('/countdown', endpoint='countdown')
    return app