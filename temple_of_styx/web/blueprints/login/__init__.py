import flask as f
import sqlalchemy as s
import argon2.exceptions

from temple_of_styx.database.tables import Person
from temple_of_styx.web.extensions import ext_sqla
from temple_of_styx.web import session


blueprint = f.Blueprint('login', __name__, template_folder='templates')


@blueprint.route("/", methods=["GET", "POST", "DELETE"])
def login():
    if f.request.accept_mimetypes.accept_html:
        match f.request.method: 
            # Display login form
            case "GET":
                return f.render_template("login.html")
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
                session.login(person=person)
            # Log out
            case "DELETE":
                session.logout() 
            # Invalid method
            case _:
                return f.abort(405)
        # Display form
        return f.render_template("login.html") 
    else:
        return f.abort(406)
