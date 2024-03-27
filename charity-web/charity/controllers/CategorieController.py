from charity.models.categorie import Categorie
from flask import jsonify,request
from extensions import db

class CategorieController:
      def __init__(self) :
            self.categorie_model=Categorie
      def create(self):
        try:
            data = request.get_json()
            nouvelle_categorie = self.categorie_model(libelle=data['libelle'],description=data['description'])
            db.session.add(nouvelle_categorie)
            db.session.commit()
            return jsonify({'message': 'Nouvelle catégorie créée avec succès'}), 201
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
        
#Récupère toutes les catégories 

      def all(self):
        try:
            categories = Categorie.query.all()
            result = [{'id': categorie.id, 'libelle': categorie.libelle,'description':categorie.description} for categorie in categories]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 50
        
# update les donnes

      def update(self,id):
          try:
              categorie=Categorie.query.get(id)
              print(Categorie)
              if not categorie:
                   return jsonify({"message":"La categorie n\'existe pas"}),404
              data=request.get_json()
              for key,value in data.items():
                setattr(categorie,key,value)
              db.session.commit()
              return jsonify({"message": "Mise à jour réussie"}),200   
          except Exception as e:
             db.session.rollback()
             return jsonify({"message":str(e)}),500    
         
#delete categorie
      def delete(self,id):
          try:
               categorie=Categorie.query.get(id)
               if not categorie:
                   return jsonify({"message":"La categorie n\'existe pas"}),404
               db.session.delete(categorie)
               db.session.commit()
               return jsonify({"message": "sucess dellete "}),200   
          except Exception as e:
             db.session.rollback()
             return jsonify({"message":str(e)}),500    
         
               
               
            
               
              
             


                            
