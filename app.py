from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://rossbuchan@localhost:5432/glove_shop_app"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers.shop_controller import gloves_blueprint
app.register_blueprint(gloves_blueprint)