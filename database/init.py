import os
from flask_sqlalchemy import SQLAlchemy

db_file = "./database/db.sqlite"


def init(app):
    file_path = os.path.abspath(db_file)
    if os.path.isfile(file_path) == False:
        f = open(file_path, "a")
        f.write("")
        f.close()
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + file_path
    return SQLAlchemy(app)
