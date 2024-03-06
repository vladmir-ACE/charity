from flask import Flask ,render_template, Blueprint,jsonify
from charity.data import projets
charity_bp=Blueprint('charity', __name__,template_folder= 'templates',static_folder='static') 



@charity_bp.route('/')
def hello_world():
    return render_template('index.html',projets=projets)

@charity_bp.route("/projet")
def getAllProject():
    return jsonify(projets)