class Arbre:
    def __init__(self, value:str, gauche:"Arbre", droite:"Arbre"):
        self.value = value
        self.gauche = gauche
        self.droite = droite

    def compte(self):
        if not self.value:
            return 0
        if self.gauche != None and self.droite != None:
            return 1 + self.gauche.compte() + self.droite.compte()
        if self.gauche != None : 
            return 1 + self.gauche.compte()
        if self.droite != None :
            return 1 + self.droite.compte()
        else:
            return 1
        
    def trouve(self,chaine):
        if not self.value:
            return False 
        
        if self.value == chaine :
            return True 
        
        if self.gauche != None and self.droite != None:
            return self.gauche.trouve(chaine) or self.droite.trouve(chaine)
        
        if self.gauche != None :
            return self.gauche.trouve(chaine)
        if self.droite != None :
            return self.droite.trouve(chaine)
        
        return False
    def valeurs_infixes(self):

        if not self.value:
            return False 
        
        if self.gauche != None and self.droite != None:
            return self.gauche.valeurs_infixes() + [self.value] + self.droite.valeurs_infixes()

        if self.gauche != None : 
            return self.gauche.valeurs_infixes() + [self.value]
        
        if self.droite != None : 
            return [self.value] + self.droite.valeurs_infixes()
        
        else:
            return [self.value]

# --------------------------------------------------------------------------------------------------
exemple = Arbre(
    "racine",
    Arbre(
        "SW-bat1",
        Arbre(
            "SW-salle1",
            Arbre(
                "SW-salle2",
                Arbre("SW-salle3", None, Arbre("SW-salle4", None, None)),
                None,
            ),
            Arbre("SW-salle5", None, None),
        ),
        Arbre(
            "SW-bat2",
            Arbre(
                "SW-salleA",
                Arbre("SW-salleC", None, None),
                Arbre("SW-salleD", None, None),
            ),
            Arbre("SW-salleB", None, None),
        ),
    ),
    Arbre("SW-admin", Arbre("SW-serveurs", None, None), Arbre("SW-backup", None, None)),
)
# ------------------------------------------------------------------------------------------------


def compte_noeuds(ABR:None):
    if not ABR:
        return 0
    
    if ABR.gauche != None and ABR.droite != None : 
        return 1 + compte_noeuds(ABR.gauche) + compte_noeuds(ABR.droite)
    
    if ABR.gauche != None:
        return 1 + compte_noeuds(ABR.gauche)
    if ABR.droite != None:
        return 1 + compte_noeuds(ABR.droite)
    
    else:
        return 1

assert(exemple.compte()==15)
assert(exemple.trouve("lol")== False)
assert(exemple.trouve("SW-salleD")== True)
assert(exemple.valeurs_infixes()==['SW-salle3', 'SW-salle4', 'SW-salle2', 'SW-salle1', 'SW-salle5', 'SW-bat1', 'SW-salleC', 'SW-salleA', 'SW-salleD', 'SW-bat2', 'SW-salleB', 'racine', 'SW-serveurs', 'SW-admin', 'SW-backup'])


def trouve_arbre(ABR:"Arbre", chaine:str)->bool:
    if not ABR:
        return False
    
    if ABR.value == chaine:
        return True
    
    if ABR.gauche != None and ABR.droite != None : 
        return trouve_arbre(ABR.gauche,chaine) or trouve_arbre(ABR.droite,chaine)
    
    if ABR.gauche != None:
        return trouve_arbre(ABR.gauche,chaine)
    
    if ABR.droite != None:
        return trouve_arbre(ABR.droite,chaine)
    
    return False

# print(trouve_arbre(Arbre("aaa", Arbre("bbb", None, None), None), "bbb"))
# print (trouve_arbre(exemple, "SW-salleA"))
# print(trouve_arbre(exemple, "pouet"))

def valeurs_infixe(ABR:"Arbre")->list:
    if not ABR:
        return []
    
    if ABR.gauche != None and ABR.droite != None:
        return valeurs_infixe(ABR.gauche) + [ABR.value] + valeurs_infixe(ABR.droite)
        
    if ABR.gauche != None : 
        return valeurs_infixe(ABR.gauche) + [ABR.value]
    
    if ABR.droite != None :
        return [ABR.value] + valeurs_infixe(ABR.droite)
    
    else :
        return [ABR.value]
    
# print(valeurs_infixe(exemple))
