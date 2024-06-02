from flask import Flask, jsonify ,render_template, Blueprint
#from charity.data import projets

from charity import charity_web

from flask import render_template , request,  redirect,  url_for,  flash

from charity.controllers.projetController import ProjetController 
from extensions import db
from charity.models.Don import Don
from charity.models.projet import Projet
import requests

projetController=ProjetController()


@charity_web.route('/')
def index():
    projets = projetController.getAll()
    return render_template('index.html',projets=projets)


@charity_web.route('/projet/<int:id>')
def detail(id):
    projet = Projet.query.get_or_404(id)
    
    total_dons=calculer_total_dons(id)
    
    
    
    
    # projetController.get(id)
    # projet = {
    #     "id": response.id,
    #     "libelle": response.libelle,
    #     "description": response.description,
    #     "categorie": response.categorie.libelle,
    #     "image": response.image,
    # }
    
    return render_template('detail.html', projet=projet,total_dons=total_dons)  # Encapsulez le projet dans un dictionnaire
    
    
def calculer_total_dons(id):
    projet = Projet.query.get_or_404(id)
    dons=projet.dons
    total_dons=0
    for don in dons:
        print(don.montant)
        total_dons +=don.montant
    return total_dons
    
    

@charity_web.route('/don', methods=['GET', 'POST'])
def faire_un_don():
    if request.method == 'POST':
        try:
            projet = request.form['projet_id']
            name = request.form['name']
            montant = request.form['montant']
            numero = request.form['numero']
            moyen = request.form['moyen_paiement']
            new_don = Don(name=name,montant=montant,numero=numero,moyen_paiement=moyen,projet_id=projet)
           
            
            # paygate_url = "https://paygateglobal.com/api/v1/pay" # URL de l'API Paygate
            # reponse = requests.post(paygate_url, json = {
            #     "auth_token": "9159f06e-3c90-4a22-b382-08cb2d1b73bc",
            #     "phone_number": numero,
            #     "amount": montant,
            #     "identifier": name,
            #     "network": moyen
            # }) # Envoi de la requête POST à l'API Paygate
            # reponse_data = reponse.json() # Convertir la reponse en json
            #print('response ',reponse_data)
            db.session.add(new_don)
            db.session.commit()
            
            total_dons=calculer_total_dons(projet)
            
            return jsonify({"success":True,"total_dons":total_dons})
        except Exception as e:
            print(e)
            
            return jsonify({"success":False,})
    return render_template('detail.html')
