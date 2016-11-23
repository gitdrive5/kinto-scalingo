#!/usr/bin/env python
import os

from paste.deploy import loadapp
from waitress import serve

if __name__ == "__main__":
    app_name = os.environ.get("APP", "app")
    port = int(os.environ.get("PORT", 5000))
    host = "0.0.0.0"

    database = os.getenv("DATABASE_URL")

    if not database:
        raise ValueError("DATABASE_URL is not correctly defined: %s" %
                         database)

    app = loadapp('config:kinto.ini', relative_to='.')

    print "[", app_name, "] application starting on https://", host, ":", port

    serve(app, host=host, port=port)
