#!/usr/bin/env python

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from notecast.user import login_required
from notecast.database import get_database

# These are named "casts" instead of "notecasts" to avoid conflict with project name
blueprint = Blueprint('cast', __name__, url_prefix="/cast")

@blueprint.route("/")
def index():
    database = get_database()

    casts = database.execute(
        "SELECT c.id, title, script, created, author_id, email"
        "FROM cast c JOIN user u ON c.author_id = u.id"
        "ORDER BY created DESC"
    ).fetchall()

    return render_template("cast/index.html", casts=casts)
