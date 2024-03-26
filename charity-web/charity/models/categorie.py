from extensions import db

class Categorie(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    libelle=db.Column(db.String(255), nullable=False)
    description=db.Column(db.String(255), nullable=False)
    