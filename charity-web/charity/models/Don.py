from extensions import db

class Don(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    montant = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.String(255), nullable=False)
    moyen_paiement = db.Column(db.String(255),nullable=False)
    projet_id = db.Column(db.Integer, db.ForeignKey('projet.id'),nullable=False)
    projet = db.relationship('Projet', backref= db.backref('dons', lazy=True))
    