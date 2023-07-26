from flask import Flask, Blueprint, redirect, render_template, request
from app import db
from models import Glove, Customer

gloves_blueprint = Blueprint("gloves", __name__)

@gloves_blueprint.route("/gloves")
def gloves():
    gloves = Glove.query.all()
    return render_template("gloves.jinja", gloves=gloves)