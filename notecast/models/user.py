#!/usr/bin/env python

from werkzeug.security import check_password_hash, generate_password_hash
from notecast.database import get_database
from email_validator import validate_email, EmailNotValidError

from flask import redirect, url_for


def create_user(email, password):
    database = get_database()
    error = None

    if not email:
        error = "An email address is required"
    elif not password:
        error = "A password is required"
    elif valid(email, password) is not None:
        error = valid(email, password)

    if error is None:
        try:
            database.execute(
                "INSERT INTO user (email, password) VALUES (?, ?)",
                (email, generate_password_hash(password)),
            )
            database.commit()
        except database.IntegrityError:
            error = f"A user with that email address already exists."

    return error


def authenticate_user(email, password):
    database = get_database()
    error = None

    user = database.execute("SELECT * FROM user WHERE email = ?", (email,)).fetchone()

    if user is None:
        error = "A user with that email does not exist"
    elif not check_password_hash(user["password"], password):
        error = "Email or password is incorrect."

    return error, user


def get_user(id):
    user = get_database().execute("SELECT * FROM user WHERE id = ?", (id,)).fetchone()

    return user


def valid(email, password):
    error = None

    try:
        if validate_email(email):
            if len(password) < 6:
                return "Password is too short"
    except EmailNotValidError as e:
        return "Your email is invalid"
