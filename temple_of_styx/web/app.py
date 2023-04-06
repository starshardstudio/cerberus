import flask as f

from temple_of_styx.config import DATABASE_URL, FLASK_SECRET_KEY
from .decorators import json
from .extensions import ext_sqla, ext_auth


app = f.Flask(__name__)

app.config["SECRET_KEY"] = FLASK_SECRET_KEY.__wrapped__
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL.__wrapped__

ext_sqla.init_app(app)
ext_auth.init_app(app)


@app.route("/healthcheck")
@json
def healthcheck():
    return True


# Running this will run the app in debug mode.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
