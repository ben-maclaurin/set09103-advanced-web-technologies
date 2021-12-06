#!/usr/bin/env python

import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from notecast.database import get_database
from notecast.models.user import create_user, authenticate_user, get_user

blueprint = Blueprint("user", __name__, url_prefix="/user")


@blueprint.before_app_request
def assign_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = get_user(user_id)


@blueprint.route("/signup", methods=("GET", "POST"))
def sign_up():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        result = create_user(email, password)

        if result is not None:
            flash(result)
        else:
            return redirect(url_for("user.login"))

    return render_template("user/signup.html")


@blueprint.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        result = authenticate_user(email, password)

        if result is not None:
            flash(result)
    else:
        session.clear()
        session["user_id"] = user["id"]
        return redirect(url_for("index"))

    return render_template("user/login.html")


@blueprint.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


def protected(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("user.login"))

        return view(**kwargs)

    return wrapped_view
