from flask import Flask ,render_template, Blueprint
from charity.data import projets
charity_bp=Blueprint('charity', __name__)

@charity_bp.route('/')
def hello_world():
    return render_template('index.html',projets=projets)
