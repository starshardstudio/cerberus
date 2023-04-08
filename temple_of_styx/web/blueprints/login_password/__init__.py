import flask as f
import sqlalchemy as s
import argon2.exceptions

from temple_of_styx.database.tables import Person
from temple_of_styx.web.extensions import ext_sqla


blueprint = f.Blueprint('login_password', __name__, template_folder='templates')


@blueprint.route("/", methods=["GET", "POST"])
def login():
    if f.request.accept_mimetypes.accept_html:
        match f.request.method: 
            case "GET":
                return f.render_template("login.html")
            case "POST":
                username = f.request.form["username"]
                password = f.request.form["password"]

                person: Person = ext_sqla.session.execute(s.select(Person).where(Person.name == username)).scalar()
                if not person:
                    f.flash("Invalid username or password.", "red")
                    return f.render_template("login.html")
                
                if not person.check_password(password):
                    f.flash("Invalid username or password.", "red")
                    return f.render_template("login.html")

                f.flash(f"Login would've been successful.")
                return f.render_template("login.html")
            case _:
                return f.abort(405)
    else:
        return f.abort(406)
