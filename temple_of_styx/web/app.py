import flask as f
import pkg_resources
import werkzeug.middleware.proxy_fix

from temple_of_styx.config import DATABASE_URL, FLASK_SECRET_KEY, STYX_BLUELIB_COLORS, STYX_TITLE, WERKZEUG_PROXY_FOR_COUNT, WERKZEUG_PROXY_PROTO_COUNT, WERKZEUG_PROXY_HOST_COUNT, WERKZEUG_PROXY_PREFIX_COUNT
from .extensions import ext_sqla, ext_login, ext_auth
from .blueprints import health, login, info


app = f.Flask(__name__)

app.wsgi_app = werkzeug.middleware.proxy_fix.ProxyFix(
    app.wsgi_app,
    x_for=WERKZEUG_PROXY_FOR_COUNT.__wrapped__,
    x_proto=WERKZEUG_PROXY_PROTO_COUNT.__wrapped__,
    x_host=WERKZEUG_PROXY_HOST_COUNT.__wrapped__,
    x_prefix=WERKZEUG_PROXY_PREFIX_COUNT.__wrapped__
)

app.config["SECRET_KEY"] = FLASK_SECRET_KEY.__wrapped__
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL.__wrapped__
app.config["STYX_BLUELIB_COLORS"] = STYX_BLUELIB_COLORS.__wrapped__
app.config["STYX_TITLE"] = STYX_TITLE.__wrapped__

ext_sqla.init_app(app)
ext_login.init_app(app)
ext_auth.init_app(app)

app.register_blueprint(health.blueprint, url_prefix="/health")
app.register_blueprint(login.blueprint, url_prefix="/login")
app.register_blueprint(info.blueprint, url_prefix="/info")


@app.before_request
def get_version():
    f.g.styx_version = pkg_resources.get_distribution("temple_of_styx").version
