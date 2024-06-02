from flask import Flask ,render_template
from flask_login import LoginManager

from charity import charity_web,charity_api,auth_bp
from flask_cors import CORS
from extensions import db

from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)

#secret key for login
app.config['SECRET_KEY'] = 'charity_secret_key',

app.register_blueprint(charity_web,url_prefix='/charity')
app.register_blueprint(charity_api,url_prefix='/api/charity')
app.register_blueprint(auth_bp,url_prefix='/auth')




# config DB port

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/charity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#initialized BD

db.init_app(app)

migrate=Migrate(app,db)


# authentification
login_manager = LoginManager()
login_manager.init_app(app)

# specification de la vue de login
login_manager.login_view = 'auth.login'


from charity.models.categorie import Categorie
from charity.models.projet import Projet
from charity.models.User import User
from charity.models.Don import Don

# with app.app_context():
#     db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

