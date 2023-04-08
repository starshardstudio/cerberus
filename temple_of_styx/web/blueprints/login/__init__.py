import flask as f
import flask_login as fl
import sqlalchemy as s

from temple_of_styx.database.tables import Person
from temple_of_styx.web.extensions import ext_sqla


blueprint = f.Blueprint('login', __name__, template_folder='templates')


@blueprint.route("/", methods=["GET", "POST", "DELETE"])
def login():
    if f.request.accept_mimetypes.accept_html:
        match f.request.method: 
            # Display login form
            case "GET":
                return f.render_template("login.html")
            # Log out
            case "DELETE":
                fl.logout_user() 
                return f.render_template("login.html") 
            # Invalid method
            case _:
                return f.abort(405)
    else:
        return f.abort(406)


@blueprint.route("/password", methods=["POST"])
def login_password():
    if f.request.accept_mimetypes.accept_html:
        match f.request.method: 
            # Log in
            case "POST":
                username = f.request.form["username"]
                password = f.request.form["password"]

                person: Person = ext_sqla.session.execute(s.select(Person).where(Person.name == username)).scalar()
                if not person:
                    f.flash("Invalid username or password.", "red")
                    return f.render_template("login.html"), 401
                
                if not person.check_password(password):
                    f.flash("Invalid username or password.", "red")
                    return f.render_template("login.html"), 401

                f.flash(f"Login successful! You are now logged in as {person.name}!", "green")
                fl.login_user(person)
                return f.render_template("login.html") 
            # Invalid method
            case _:
                return f.abort(405)
    else:
        return f.abort(406)
