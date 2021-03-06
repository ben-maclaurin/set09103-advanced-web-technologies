#!/usr/bin/env python

from flask import Blueprint, flash, g, redirect, render_template, request, url_for

from werkzeug.exceptions import abort

from notecast.controllers.user import protected
from notecast.database import get_database
from notecast.models.cast import get_casts, create_cast

# These are named "casts" instead of "notecasts" to avoid conflict with project name
blueprint = Blueprint("cast", __name__, url_prefix="/")


@blueprint.route("/")
@protected
def index():
    return render_template("cast/index.html", casts=get_casts(g.user["id"]))


@blueprint.route("/create", methods=("GET", "POST"))
@protected
def create():
    if request.method == "POST":
        title = request.form["title"]
        script = request.form["script"]
        voice = request.form["voice"]
        image = request.form["image"]

        result = create_cast(title, script, g.user["id"], voice, image)

        if result is not None:
            flash(result)
        else:
            return redirect(url_for("cast.index"))

    return render_template("cast/create.html")
