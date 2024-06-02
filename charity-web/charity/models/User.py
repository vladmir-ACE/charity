from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    
    def set_password(self, password):
        """Definit le mot de passe sous forme de hash"""
        self.password = generate_password_hash(password)
        
    def verify_password(self, password):
        """Verifie le mot de passe"""
        return check_password_hash(self.password, password)