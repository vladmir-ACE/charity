from flask import Flask ,render_template
from charity import charity_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(charity_bp,url_prefix='/charity')