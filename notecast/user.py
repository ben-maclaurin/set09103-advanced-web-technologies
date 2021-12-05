#!/usr/bin/env python

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash
from notecast.database import get_database

blueprint = Blueprint("user", __name__, url_prefix="/user")

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
