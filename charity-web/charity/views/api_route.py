from flask import Flask , Blueprint,jsonify
from charity.data import projets

from charity import charity_api
from extensions import db
from charity.controllers.CategorieController import CategorieController
from charity.controllers.projetController import ProjetController

categorie_controller=CategorieController()
projet_controller=ProjetController()

@charity_api.route("/projet")
def getAllProject():
    return jsonify(projets)


#Categorie routes

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


# projet routes 

@charity_api.route("/add_project", methods=["POST"])
def addProject():
    return projet_controller.create()

@charity_api.route("/list_project", methods=["GET"])
def listProject():
    return projet_controller.all()

@charity_api.route("/update/projet/<int:id>", methods=["PUT"])
def UpdateProjet(id):
    return projet_controller.update(id=id)

@charity_api.route("/delete/projet/<int:id>", methods=["DELETE"])
def deleteProjet(id):
    return projet_controller.delete(id=id)
