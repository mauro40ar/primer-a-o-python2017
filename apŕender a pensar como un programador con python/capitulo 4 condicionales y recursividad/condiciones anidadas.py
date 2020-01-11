def Numeros(summers):
    if summers>0:
        if summers <= 10:
            print ("el numero %s es positivo"%(summers))
    elif summers<0:
        if summers >= (-10):
            print("el numero %s es negativo"%(summers))
    else:
        print ("el numero %s es igual a 0"%(summers))

Numeros(9)

def Compara(x,y):
    if x>0:
        if x==y:
            print ("los valores %s y %s son iguales"%(x,y))
        else:
            print("los valores %s y %s son distintos "% (x,y))
Compara(10,-10)