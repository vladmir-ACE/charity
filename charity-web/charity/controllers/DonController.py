from flask import jsonify, request
from extensions import db
from charity.models.Don import Don


class DonController:
    def __init__(self):
        self.don_model = Don

    def create(self):
        try:
            data = request.get_json()
            nouveau_don = self.don_model(name=data['name'], montant=data['montant'], numero=data['numero'], moyen_paiement=data['moyen_paiement'])
            db.session.add(nouveau_don)
            db.session.commit()
            return jsonify({'message': 'Don éffectué avec succès'}), 201
        except KeyError:
            jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def all(self):
        try:
            dons = Don.query.all()
            result = [{'id': don.id, 'name': don.name, 'montant':don.montant, 'numero':don.numero, 'moyen_paiement':don.moyen_paiement} for don in dons]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def get(self, don_id):
        try:
            don = Don.query.get(don_id)
            if don:
                return don
            else:
                return None  
        except Exception as e:
            db.session.rollback()
            raise e
        
