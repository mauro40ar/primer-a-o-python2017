def Validacion(x,y):
    if x%y==0:
        return "Its %s"%(True)
    else:
        return "its %s"%(False)
print (Validacion(10,5))

def Estaentre(x,y,z):
    if y<=x<=z:
        return 1
    else:
        return 0
print (Estaentre(15,10,19))