import flask as f
import flask_sqlalchemy

from temple_of_styx.database.tables import Base
from temple_of_styx.config import DATABASE_URL
from .decorators import json


app = f.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL.__wrapped__

ext_sqla = flask_sqlalchemy.SQLAlchemy(
    app=app, 
    metadata=Base.metadata,
    add_models_to_shell=False,
)


@app.route("/healthcheck")
@json
def healthcheck():
    return f.jsonify(True)


# Running this will run the app in debug mode.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, load_dotenv=True)
