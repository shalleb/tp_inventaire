def model_product()->dict:
    """_model of product_

    Returns:
        dict: _all element that represent the product_
    """
    
    return {
       "nom":None,
       "quantite":None,
       "prix":None,     
    }

def model_inventory() ->dict:
    """model inventory

    Returns:
        dict: _all element that represent the inventory_
    """
    return {
        "produits":[]
    }
    
def afficher_inventaire(inventaire:list):
    if len(inventaire) <0:
        print("L'Inventaire est vide")
    else:
        for objet in inventaire:
            print (f"{objet["nom"]} : {objet["quantité"]}")

def ajouter_produit(produit:dict,inventaire:list):
    pass

def creation_produit(produit:dict)->dict:
    for key in produit.keys:
        produit[key]=controle_saisie(key)
    return produit

def modifier_quantite(produit:dict):
    pass

def supprimer_produit(produit:dict, inventaire:list):
    pass

def rechercher_produit(produit:dict,inventaire:list):
    pass

def valeur_totale_inventaire(inventaire:list):
    pass

def controle_champ_vide(entree:str) -> bool:
    """_Control fonction to avoid empty field_

    Args:
        entree (str): _input to control_

    Returns:
        bool: _True if input is empty, False if not empty_    
        
    """
    
    if len(entree) == 0 :
        print("Le champ ne peut être vide")
        return True
    else:
        return False

def controle_saisie(cle:str)->str:
    """_ask for input and control for an item  _

    Args:
        cle (str): _item_

    Returns:
        str: _a valid input for the item of inventory_
    """
    liste_numerique = ["quantité","prix"]
    liste_majuscule = ["nom"]
    
    while True:
        entree = input(f"Veuilez entrer le {cle}: ")
        if cle in liste_numerique and not controle_champ_vide(entree) :
            try:
                entree = float(entree)
                if entree < 0:
                    print("La valeur entrée ne peut pas être négative:")
                else:
                    break        
            except ValueError as error:
                print("La valeur entrée n'est pas un chiffre valide: ",error)
        elif cle in liste_majuscule and not controle_champ_vide(entree) :
            entree = entree.upper()
            break
    return entree 