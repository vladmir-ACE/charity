from flask import Flask ,render_template
from charity import charity_bp

app = Flask(__name__,template_folder='charity/templates',static_folder='charity/static')

app.register_blueprint(charity_bp,url_prefix='')