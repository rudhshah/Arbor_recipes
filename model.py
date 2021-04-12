"""Insta485 model (database) API."""
import sqlite3
import uuid
import hashlib
import pathlib
import os
import flask
import ArborRecipe


def delete_file(filename):
    """Delete file from uploads folder."""
    if os.path.exists(os.path.join(
            ArborRecipe.app.config['UPLOAD_FOLDER'], filename)):
        os.remove(os.path.join(ArborRecipe.app.config['UPLOAD_FOLDER'], filename))


def upload_file(fileobj):
    """Upload file to uploads folder and return unique identifier/filename."""
    filename = fileobj.filename

    # Compute base name (filename without directory).  We use a UUID to avoid
    # clashes with existing files, and ensure that the name is compatible with
    # the filesystem.
    uuid_basename = "{stem}{suffix}".format(
        stem=uuid.uuid4().hex,
        suffix=pathlib.Path(filename).suffix
    )

    # Save to disk
    path = ArborRecipe.app.config["UPLOAD_FOLDER"] / uuid_basename
    fileobj.save(path)
    return uuid_basename


def get_salted_hash(password, used_salt=None):
    """Return salted hashed password to save in database."""
    algorithm = 'sha512'
    salt = used_salt
    # if no used salt make new one
    if salt is None:
        salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string


def get_salt(username):
    """Return Salt for username."""
    connection = ArborRecipe.model.get_db()

    cur = connection.execute(
        "SELECT password FROM users WHERE username = '{0}' ".format(username)
    )
    return cur.fetchall()[0]['password'].split('$')[1]


def dict_factory(cursor, row):
    """Convert database row objects to a dictionary keyed on column name.

    This is useful for building dictionaries which are then used to render a
    template.  Note that this would be inefficient for large queries.
    """
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def get_db():
    """Open a new database connection.

    Flask docs:
    https://flask.palletsprojects.com/en/1.0.x/appcontext/#storing-data
    """
    if 'sqlite_db' not in flask.g:
        db_filename = ArborRecipe.app.config['DATABASE_FILENAME']
        flask.g.sqlite_db = sqlite3.connect(str(db_filename))
        flask.g.sqlite_db.row_factory = dict_factory

        # Foreign keys have to be enabled per-connection.  This is an sqlite3
        # backwards compatibility thing.
        flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")

    return flask.g.sqlite_db


@ArborRecipe.app.teardown_appcontext
def close_db(error):
    """Close the database at the end of a request.

    Flask docs:
    https://flask.palletsprojects.com/en/1.0.x/appcontext/#storing-data
    """
    assert error or not error  # Needed to avoid superfluous style error
    sqlite_db = flask.g.pop('sqlite_db', None)
    if sqlite_db is not None:
        sqlite_db.commit()
        sqlite_db.close()
