from flask import Flask ,render_template

from charity import charity_web,charity_api
from flask_cors import CORS
from extensions import db

app = Flask(__name__)
CORS(app)

app.register_blueprint(charity_web,url_prefix='/charity')
app.register_blueprint(charity_api,url_prefix='/api/charity')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/charity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initialized BD

db.init_app(app)

from charity.models.categorie import Categorie
from charity.models.projet import Projet

with app.app_context():
    db.create_all()


