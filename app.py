from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://rossbuchan@localhost:5432/glove_shop_app"
db = SQLAlchemy(app)
migrate = Migrate(app, db)