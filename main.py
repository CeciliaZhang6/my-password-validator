import flask


# TODO: change this to your academic email
AUTHOR = "czhang6@brynmawr.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    # FIXME: to be implemented
    special_chars = "!@#$%^&*"
    digits = "0123456789"

    special_chars = "!@#$%^&*"
    digits = "0123456789"

    if len(pw) < 8:
        return flask.jsonify({"valid": False, "reason": "Password too short"}), 200
    elif not any(char.isupper() for char in pw):
        return flask.jsonify({"valid": False, "reason": "Password must contain at least one uppercase letter"}), 200
    elif not any(char in special_chars for char in pw):
        return flask.jsonify({"valid": False, "reason": "Password must contain at least one special character"}), 200
    elif not any(char in digits for char in pw):
        return flask.jsonify({"valid": False, "reason": "Password must contain at least one digit"}), 200
    else:
        return flask.jsonify({"valid": True, "reason": "Password is valid"}), 200

    return flask.jsonify({"valid": False, "reason": "Not implemented"}), 501
