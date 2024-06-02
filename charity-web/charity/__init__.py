from flask import  Blueprint

charity_web=Blueprint('charity_web', __name__,template_folder= 'templates',static_folder='static') 
charity_api=Blueprint('charity_api', __name__,static_folder='static') 
auth_bp = Blueprint('auth', __name__, template_folder = 'templates')

from charity.views import route
from charity.views import api_route
from charity.views import auth_route

