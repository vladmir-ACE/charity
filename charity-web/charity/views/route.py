from flask import Flask ,render_template, Blueprint
from charity.data import projets

from charity import charity_web


@charity_web.route('/')
def hello_world():
    return render_template('index.html',projets=projets)
