#!/usr/bin/env python
from notecast.database import get_database
from notecast.lib.speech import synthesise_speech
import uuid
import os


def get_casts(user_id):
    database = get_database()

    casts = database.execute(
        "SELECT * FROM cast WHERE author_id=" + str(user_id) + " ORDER BY created DESC"
    ).fetchall()

    return casts


def create_cast(title, script, user_id, voice):
    error = None

    if not title:
        error = "A title is required"
    elif not script:
        error = "A script is required"
    elif len(script) > 500:
        error = "Script is too long"
    else:
        database = get_database()

        name = str(uuid.uuid4())

        database.execute(
            "INSERT INTO cast (title, script, location, author_id)"
            "VALUES (?, ?, ?, ?)",
            (title, script, os.environ.get("BUCKET_URL") + name + ".mp3", user_id),
        )

        database.commit()

        synthesise_speech(script, name, voice)

    return error
