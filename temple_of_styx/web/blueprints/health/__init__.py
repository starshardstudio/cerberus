import flask as f

from temple_of_styx.web.decorators import json


blueprint = f.Blueprint('health', __name__, template_folder='templates')


@blueprint.route("/healthcheck")
@json
def healthcheck():
    return True


__all__ = (
    "blueprint",
)
