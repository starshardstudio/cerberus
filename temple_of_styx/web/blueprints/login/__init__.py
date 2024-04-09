import flask as f
import flask_login as fl
import sqlalchemy as s

from temple_of_styx.database.tables import Person
from temple_of_styx.web.extensions import ext_sqla

blueprint = f.Blueprint('login', __name__, template_folder='templates')


@blueprint.route("/", methods=["GET", "POST"])
def login():
    if f.request.accept_mimetypes.accept_html:
        match f.request.method:
            # Display login form
            case "GET":
                return f.render_template("login.html")
            # Process login form
            case "POST":
                # Find the username used to login
                username = f.request.form.get("username")
                if not username:
                    f.flash("Missing username.", "red")
                    return f.render_template("login.html")
                # Find the Person to login as
                person: Person = ext_sqla.session.execute(s.select(Person).where(Person.name == username)).scalar()
                if not person:
                    f.flash("Invalid username.", "red")
                    return f.render_template("login.html")
                # noinspection PyUnreachableCode
                # Login via password
                if person.has_password():
                    f.session["username"] = username
                    return f.redirect(f.url_for("login.login_password"))
                # TODO: Login via passkey
                elif person.has_passkey():
                    f.session["username"] = username
                    return f.redirect(f.url_for("login.login_passkey"))
                # No available login methods
                else:
                    f.flash("No available login methods.", "red")
                    return f.render_template("login.html")
            # Invalid method
            case _:
                return f.abort(405)
    # Unsupported mime type
    else:
        return f.abort(406)


@blueprint.route("/password", methods=["GET", "POST"])
def login_password():
    if f.request.accept_mimetypes.accept_html:
        # Find the username used to login
        username = f.session.get("username")
        if not username:
            f.flash("Malformed session.", "red")
            return f.redirect(f.url_for("login.login"))
        # Find the Person to login as
        person: Person = ext_sqla.session.execute(s.select(Person).where(Person.name == username)).scalar()
        if not person:
            f.flash("Could not find user referenced in session.", "red")
            return f.redirect(f.url_for("login.login"))

        match f.request.method:
            # Display the password login form
            case "GET":
                return f.render_template("password.html", selected_user=person)
            # Authenticate via password
            case "POST":
                # Find the entered password
                password = f.request.form.get("password")
                if not password:
                    f.flash("Missing password.", "red")
                    return f.redirect(f.url_for("login.login_password"))
                # Check the entered password
                if not person.check_password(password):
                    f.flash("Invalid password.", "red")
                    return f.redirect(f.url_for("login.login_password"))
                # Complete login
                f.flash(f"Login successful! You are now logged in as {person.name}!", "green")
                fl.login_user(person)
                del f.session["username"]
                return f.redirect(f.url_for("info.info"))
            # Invalid method
            case _:
                return f.abort(405)
    else:
        return f.abort(406)


@blueprint.route("/passkey", methods=["GET", "POST"])
def login_passkey():
    if f.request.accept_mimetypes.accept_html:
        # Find the username used to login
        username = f.session.get("username")
        if not username:
            f.flash("Malformed session.", "red")
            return f.redirect(f.url_for("login.login"))
        # Find the Person to login as
        person: Person = ext_sqla.session.execute(s.select(Person).where(Person.name == username)).scalar()
        if not person:
            f.flash("Could not find user referenced in session.", "red")
            return f.redirect(f.url_for("login.login"))

        match f.request.method:
            # Display the password login form
            case "GET":
                return f.render_template("passkey.html", selected_user=person)
            # TODO: Authenticate via passkey
            case "POST":
                return f.abort(500)
                f.flash(f"Login successful! You are now logged in as {person.name}!", category="green")
                fl.login_user(person)
                del f.session["username"]
                return f.redirect(f.url_for("info.info"))
            # Invalid method
            case _:
                return f.abort(405)
    else:
        return f.abort(406)


@blueprint.route("/logout", methods=["POST"])
def logout():
    if f.request.accept_mimetypes.accept_html:
        match f.request.method:
            # Log out
            case "POST":
                fl.logout_user()
                f.flash(f"Logout successful!", "green")
                return f.redirect(f.url_for("login.login"))
            # Invalid method
            case _:
                return f.abort(405)
    # Unsupported mime type
    else:
        return f.abort(406)
