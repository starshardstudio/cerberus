import flask as f
import flask_login as fl
import sqlalchemy as s

from temple_of_styx.database.tables import Person
from temple_of_styx.web.extensions import ext_sqla, ext_login


blueprint = f.Blueprint('info', __name__, template_folder='templates')


@blueprint.route("/")
def info():
    if f.request.accept_mimetypes.accept_html:
        if not fl.current_user.is_authenticated:
            return f.abort(401)
        return f.render_template("info.html")
    elif f.request.accept_mimetypes.accept_json:
        raise NotImplementedError("TODO")
    else:
        return f.abort(406)