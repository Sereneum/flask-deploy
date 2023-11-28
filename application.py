from flask import Flask


def create_app():
    app = Flask(__name__)

    from server import server_app

    app.register_blueprint(server_app)

    return app
