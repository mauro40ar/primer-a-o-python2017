#escribir una funcion comparar que devuelva 1 si x>y, 0 si x==y, y -1 si y>x
def Comparar(x,y):
    if x>y:
        return 1
    elif x<y:
        return -1
    else:
        return 0
print(Comparar(9,9))