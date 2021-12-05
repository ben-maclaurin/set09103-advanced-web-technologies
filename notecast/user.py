#!/usr/bin/env python

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash
from notecast.database import get_database

blueprint = Blueprint("user", __name__, url_prefix="/user")

@blueprint.before_app_request
def assign_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = get_database().execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()

@blueprint.route("/signup", methods=("GET", "POST"))
def sign_up():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        database = get_database()
        error = None

        if not email:
            error = "An email address is required"
        elif not password:
            error = "A password is required"

        if error is None:
            try:
                database.execute(
                    "INSERT INTO user (email, password) VALUES (?, ?)",
                    (email, generate_password_hash(password)),
                )
                database.commit()
            except database.IntegrityError:
                error = f"A user with that email address already exists."
            else:
                return redirect(url_for("user.login"))
        flash(error)

    return render_template("user/signup.html")

@blueprint.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("user.login"))

        return view(**kwargs)

    return wrapped_view
