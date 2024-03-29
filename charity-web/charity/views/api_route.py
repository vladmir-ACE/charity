from flask import Flask , Blueprint,jsonify
from charity.data import projets

from charity import charity_api
from extensions import db
from charity.controllers.CategorieController import CategorieController

categorie_controller=CategorieController()
@charity_api.route("/projet")
def getAllProject():
    return jsonify(projets)

@charity_api.route("/add_cat", methods=["POST"])
def addCategory():
    return categorie_controller.create()

@charity_api.route("/list_cat", methods=["GET"])
def listCategory():
    return categorie_controller.all()


@charity_api.route("/update/<int:id>", methods=["PUT"])
def UpdateCat(id):
    return categorie_controller.update(id=id)

@charity_api.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    return categorie_controller.delete(id=id)




