from flask import Flask, g
from .app_factory import create_app
from .db_connect import close_db, get_db

app = create_app()
app.secret_key = 'my-super-secret'  # Replace with an environment variable

# Register Blueprints
# from app.blueprints.runners import runners
from app.blueprints.samples import samples

# app.register_blueprint(runners)
app.register_blueprint(samples)

from . import routes

@app.before_request
def before_request():
    g.db = get_db()

# Setup database connection teardown
@app.teardown_appcontext
def teardown_db(exception=None):
    close_db(exception)

