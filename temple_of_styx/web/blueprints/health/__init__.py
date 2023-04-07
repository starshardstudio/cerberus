import flask as f

from temple_of_styx.web.decorators import json


blueprint = f.Blueprint('health', __name__, template_folder='templates')


@blueprint.route("/healthcheck")
def healthcheck():
    if f.request.accept_mimetypes.accept_json:
        return f.jsonify(True)
    return f.render_template("healthcheck.html")


__all__ = (
    "blueprint",
)
