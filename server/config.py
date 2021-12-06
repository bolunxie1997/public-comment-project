import os
from datetime import timedelta

SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite3"
SQLALCHEMY_TRACK_MODIFICATIONS=False
PERMANENT_SESSION_LIFETIME = timedelta(days=2)
SECRET_KEY= os.urandom(24)

