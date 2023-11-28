from flask import Blueprint

server_app = Blueprint("server_app", __name__)


@server_app.route("/")
def hello_world():
    return ".URBAN GUARD."
