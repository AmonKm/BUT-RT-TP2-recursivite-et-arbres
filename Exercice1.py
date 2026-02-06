# Prend un entier strictement positif en argument et renvoie sa représentation binaire
def int2bin(n:int)->str:
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    return int2bin(n//2) + str(n%2)

assert(int2bin(6)== "110")

# Transformation inverse
def bin2int(s:str)-> int:
    if len(s) == 1 and s == '0':
        return 0
    elif len(s) == 1 and s == '1':
        return 1
    return int(s[0])*2**(len(s)-1) + bin2int(s[1:len(s)])

assert(bin2int("10010")==18)
