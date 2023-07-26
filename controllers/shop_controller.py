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
    
@gloves_blueprint.route("/gloves/new")
def new_glove():
    return render_template("new_glove.jinja")

@gloves_blueprint.route("/gloves", methods=['POST'])
def add_glove():
    size = request.form['size']
    colour = request.form['colour']
    price = request.form['price']

    glove = Glove(size=size, colour=colour, price=price)

    db.session.add(glove)
    db.session.commit()
    return redirect("/gloves")

@gloves_blueprint.route("/gloves/<id>/edit")
def edit_glove(id):
    glove = Glove.query.get(id)
    return render_template("edit_glove.jinja", glove=glove)

@gloves_blueprint.route("/gloves/<id>", methods=['POST'])
def update_glove(id):
    size = request.form['size']
    colour = request.form['colour']
    price = request.form['price']

    glove = Glove.query.get(id)

    glove.size = size
    glove.colour = colour
    glove.price = price

    db.session.commit()
    return redirect("/gloves")

@gloves_blueprint.route("/gloves/<id>/delete")
def delete_glove(id):
    glove = Glove.query.get(id)

    db.session.delete(glove)
    db.session.commit()

    return redirect("/gloves")
