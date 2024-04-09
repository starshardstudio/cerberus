import flask as f
import flask_login as fl
import webauthn

from temple_of_styx.database.tables import Person
from temple_of_styx.web.extensions import ext_sqla
from temple_of_styx.config import STYX_TITLE, STYX_ID


blueprint = f.Blueprint('info', __name__, template_folder='templates')


@blueprint.route("/")
def info():
    if f.request.accept_mimetypes.accept_html:
        if not fl.current_user.is_authenticated:
            return f.render_template("unauthenticated.html"), 401
        return f.render_template("info.html")
    elif f.request.accept_mimetypes.accept_json:
        if not fl.current_user.is_authenticated:
            return f.jsonify({"error": "Not authenticated"}), 401
        user: Person = fl.current_user
        return f.jsonify({
            "name": user.name,
            "avatar": user.avatar
        })
    else:
        return f.abort(406)


@blueprint.route("/passwd", methods=["POST"])
def passwd():
    if f.request.accept_mimetypes.accept_html:
        # Ensure that the user is logged in
        if not fl.current_user.is_authenticated:
            f.flash("You cannot change password while not authenticated.", category="red")
            return f.redirect(f.url_for("info.info"))
        # Get the value of the current password
        current = f.request.form.get("current")
        if not current:
            f.flash("Missing current password.", category="red")
            return f.redirect(f.url_for("info.info"))
        # Ensure the current password is correct
        if not fl.current_user.check_password(current):
            f.flash("Incorrect current password.", category="red")
            return f.redirect(f.url_for("info.info"))
        # Get the value of the password field
        password1 = f.request.form.get("password1")
        if not password1:
            f.flash("Missing new password.", category="red")
            return f.redirect(f.url_for("info.info"))
        # Get the value of the confirm password field
        password2 = f.request.form.get("password2")
        if not password2:
            f.flash("Missing confirm password.", category="red")
            return f.redirect(f.url_for("info.info"))
        # Make sure the two values match
        if password1 != password2:
            f.flash("Entered passwords do not match.", category="red")
            return f.redirect(f.url_for("info.info"))
        # Actually change the password
        fl.current_user.set_password(password1)
        ext_sqla.session.commit()
        f.flash("Password changed successfully!", category="green")
        return f.redirect(f.url_for("info.info"))
    elif f.request.accept_mimetypes.accept_json:
        # Ensure that the user is logged in
        if not fl.current_user.is_authenticated:
            return f.jsonify({"error": "Not authenticated"}), 401
        raise NotImplementedError("TODO")
    else:
        return f.abort(406)


@blueprint.route("/passkey", methods=["POST"])
def passkey():
    if f.request.accept_mimetypes.accept_json:
        # Ensure that the user is logged in
        if not fl.current_user.is_authenticated:
            return f.jsonify({"error": "Not authenticated"}), 401
        user: Person = fl.current_user
        # TODO: Challenges should be more complex, see https://security.stackexchange.com/questions/268308/how-to-properly-manage-webauthn-challenges
        user.generate_passkey_challenge()
        ext_sqla.session.commit()
        # Generate the registration options
        regopts = webauthn.generate_registration_options(
            rp_id=STYX_ID.__wrapped__,
            rp_name=STYX_TITLE.__wrapped__,
            user_id=bytes(user.get_id(), encoding="utf8"),
            user_name=user.name,
        )
        # Return the registration options
        return f.jsonify(webauthn.options_to_json(regopts))
    else:
        return f.abort(406)
