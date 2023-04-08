import flask as f
import pkg_resources

from temple_of_styx.config import DATABASE_URL, FLASK_SECRET_KEY, STYX_BLUELIB_COLORS, STYX_TITLE
from .decorators import json
from .extensions import ext_sqla, ext_auth
from .blueprints import health, login_password


app = f.Flask(__name__)

app.config["SECRET_KEY"] = FLASK_SECRET_KEY.__wrapped__
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL.__wrapped__
app.config["STYX_BLUELIB_COLORS"] = STYX_BLUELIB_COLORS.__wrapped__
app.config["STYX_TITLE"] = STYX_TITLE.__wrapped__

ext_sqla.init_app(app)
ext_auth.init_app(app)

app.register_blueprint(health.blueprint, url_prefix="/health")
app.register_blueprint(login_password.blueprint, url_prefix="/login/password")

@app.before_request
def get_version():
    f.g.styx_version = pkg_resources.get_distribution("temple_of_styx").version

# Running this will run the app in debug mode.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
