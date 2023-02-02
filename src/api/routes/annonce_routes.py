
from flask import Blueprint
from src.api.controllers.annonce_controller import AddAnnonce,DeleteAnnonce, getAllAnnonces, getAnnonceDetails, SearchForAnnonce,getTypes
from src.api.auth.auth import requires_auth


annonce_bp = Blueprint("annonce_bp", __name__)

@annonce_bp.get('/')
def get_annonces():
    return getAllAnnonces()

'''
ce route c'est pour avoir les details d'une annonce
'''


@annonce_bp.get('/<annonceId>')
def get_Annonce_Details(annonceId):
    return getAnnonceDetails(annonceId)

'''
route pour ajouter une annonce
'''
@annonce_bp.route('/',methods=['POST'])
@requires_auth
def Add_Annonce(user):
    return AddAnnonce(user)


'''
route pour supprimer une annonce
'''
@annonce_bp.delete('/<annonceId>')
@requires_auth
def Delete_Annonce(user,annonceId):

    return DeleteAnnonce(user,annonceId)
'''
route pour chercher une annonce
'''
@annonce_bp.route('/search')
def Search_Annonce():
    return SearchForAnnonce()

@annonce_bp.route('/types')
def GetTypes():
    return getTypes()
