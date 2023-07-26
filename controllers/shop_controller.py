from flask import Flask, Blueprint, redirect, render_template, request
from app import db
from models import Glove, Customer

gloves_blueprint = Blueprint("gloves", __name__)

@gloves_blueprint.route("/gloves")
def gloves():
    gloves = Glove.query.all()
    return render_template("gloves.jinja", gloves=gloves)

@gloves_blueprint.route("/gloves/<id>")
def get_glove(id):
    glove = Glove.query.get(id)
    gloves = Glove.query.all()
    if glove in gloves:
        return render_template("show_glove.jinja", glove=glove)
    else:
        return "This glove doesnt exist!"