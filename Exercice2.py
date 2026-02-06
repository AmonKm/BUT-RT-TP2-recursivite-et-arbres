# Dichotomie
def trouve_liste(ma_liste:list,num:int)->bool:

    if len(ma_liste) == 1:
        return num == ma_liste[0]
    
    elif num == ma_liste[len(ma_liste)//2]:
        return True
    
    elif num < len(ma_liste)//2:
        return trouve_liste(ma_liste[0:len(ma_liste)//2],num)
    
    elif num > len(ma_liste)//2:
        return trouve_liste(ma_liste[len(ma_liste)//2:len(ma_liste)],num)
    


assert(trouve_liste([1, 2, 4, 8, 12, 14, 23, 42], 9)== False)
assert(trouve_liste([1, 2, 4, 8, 12, 14, 23, 42], 23)== True)
