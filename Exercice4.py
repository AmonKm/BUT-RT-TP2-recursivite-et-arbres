class ABR:
    def __init__(self, value:str, gauche:"Arbre", droite:"Arbre"):
        self.value = value
        self.gauche = gauche
        self.droite = droite

    def trouver(self, mot:str):
        if mot == self.value:
            return True 
        
        elif self.gauche != None and self.droite != None:
            if mot >= self.value:
                return self.droite.trouver(mot)
            return self.gauche.trouver(mot)
        
        elif self.gauche != None and self.droite == None:
            return self.gauche.trouver(mot)
        
        elif self.gauche == None and self.droite != None:
            return self.droite.trouver(mot)
        
        return False

    def insere(self, mot:str):
        if self.value == None :
            self.value = mot

        elif mot >= self.value :
            if not self.droite :
                self.droite = ABR(mot, None, None)
            else:
                self.droite.insere(mot)

        elif mot <= self.value :
            if not self.gauche:
                self.gauche = ABR(mot, None, None)
            else:
                self.gauche.insere(mot)




    def __str__(self):
        if self.gauche == None and self.droite == None:
            return F"(_, '{self.value}', _)"
        
        if self.gauche == None and self.droite != None:
            return F"(_, '{self.value}', {self.droite})"
        
        if self.gauche != None and self.droite == None:
            return F"('{self.gauche}', '{self.value}' , _)"
        
        else : 
            return F"({self.gauche}), '{self.value}' ,({self.droite})"
        

exemple_abr = ABR(
    "ping",
    ABR(
        "boot",
        ABR("arm", None, None),
        ABR("json", ABR("ethernet", None, None), ABR("linux", None, None)),
    ),
    ABR("tcp", ABR("shell", None, None), ABR("yolo", None, None)),
)
# print(ABR("b", ABR("a", None, None), ABR("c", None, None)))
# print(ABR("a", None, ABR("c", None, None)))
# print(ABR("a", None, ABR("d", ABR("c", None, None), None)))

assert(exemple_abr.trouver("shell") == True)
assert(exemple_abr.trouver("linux") == True)
assert(exemple_abr.trouver("windows") == False)

# arbre = ABR("ping", None, None)
# arbre.insere("tcp")
# print(arbre)
# arbre.insere("boot")
# print(arbre)
# arbre.insere("ldap")
# print(arbre)

def abr_from_list(ma_liste:list):
    Mon_arbre = ABR(None, None, None)
    for element in ma_liste:
        Mon_arbre.insere(element)
    return Mon_arbre

liste_deouf = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii", "jjj", "kkk", "lll", "mmm", "nnn", "ooo", "ppp", "qqq"]

print(abr_from_list(liste_deouf))

import random
print(random.shuffle(liste_deouf))

arbreshuffle = abr_from_list(liste_deouf)
print(arbreshuffle)
