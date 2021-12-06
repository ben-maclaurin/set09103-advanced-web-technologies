#!/usr/bin/env python

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from notecast.user import login_required
from notecast.database import get_database

# These are named "casts" instead of "notecasts" to avoid conflict with project name
blueprint = Blueprint('cast', __name__, url_prefix="/cast")
