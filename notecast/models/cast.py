#!/usr/bin/env python
from notecast.database import get_database
from notecast.lib.speech import synthesise_speech


def get_casts():
    database = get_database()

    casts = database.execute(
        "SELECT c.id, title, script, created, author_id"
        " FROM cast c JOIN user u ON c.author_id = u.id"
        " ORDER BY created DESC"
    ).fetchall()

    return casts


def create_cast(title, script, user_id):
    error = None

    if not title:
        error = "A title is required"
    elif not script:
        error = "A script is required"
    else:
        database = get_database()

        database.execute(
            "INSERT INTO cast (title, script, author_id)" "VALUES (?, ?, ?)",
            (title, script, user_id),
        )
        database.commit()

        synthesise_speech(script)

    return error
