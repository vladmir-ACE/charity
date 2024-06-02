from charity.models.projet import Projet
from flask import jsonify,request
from extensions import db


class ProjetController:
    def __init__(self) :
            self.projet_model=Projet
    def create(self):
        try:
            libelle= request.form['libelle']
            categorie_id=request.form['categorie_id']
            description=request.form['description']
            if 'image'not in request.files:
                return jsonify({'message':'aucun fichier image'}) ,400
            
            image=request.files['image']
            
            nouvelle_projet = self.projet_model(libelle=libelle,description=description, categorie_id=categorie_id)
            nouvelle_projet.saveImg(image)
            db.session.add(nouvelle_projet)
            db.session.commit()
            return jsonify({'message': 'projet créée avec succès'}), 201
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            print(e)
            return jsonify({'erreur'}), 500
        
#Récupère toutes les catégories 

    def all(self):
        try:
            projets = Projet.query.all()
            result = [{'id': projet.id, 'libelle': projet.libelle,'description':projet.description, 'image':projet.image} for projet in projets]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 50
        
    def update(self,id):
        try:
            projet=Projet.query.get(id)
            if not projet:
                   return jsonify({"message":"La Projet n\'existe pas"}),404
            data=request.get_json()
            projet.libelle=data['libelle']           
            projet.categorie_id=data['categorie_id']
            projet.description=data['description']
            
            db.session.commit()
            return jsonify({'message': 'projet mis a jour avec succès'}), 201
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            print(e)
            return jsonify({'erreur'}), 500
        
        
    #delete project 
    def delete(self,id):
        try:
            projet=Projet.query.get(id)
            if not projet:
                   return jsonify({"message":"La Projet n\'existe pas"}),404
            db.session.delete(projet)
            db.session.commit()
            return jsonify({"message": "sucess delete "}),200   
        except Exception as e:
             print(e)
             db.session.rollback()
             return jsonify({"message":str(e)}),500    
         
         
    #  methode for flask views
    def getAll(self):
        try:
            projets = Projet.query.all()
            if not projets:
                return jsonify({'message': 'Aucun projet trouvé'}), 404
            
            result = [{'id': projet.id, 'libelle': projet.libelle, 'image': projet.image, 'description': projet.description, 'categorie_id': projet.categorie_id} for projet in projets]
            return result
        except Exception as e:
            return jsonify({'message': 'Une erreur s\'est produite lors de la récupération des projets'}), 500
        
    
    def get(self, projet_id):
        try:
            projet = Projet.query.get(projet_id)
            if projet:
                return projet
            else:
                return None  # Ou renvoyez une valeur spécifique pour indiquer que le projet n'a pas été trouvé
        except Exception as e:
            db.session.rollback()
            raise e
        