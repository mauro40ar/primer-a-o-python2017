import math
def Distancia(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    dalcuadrado=dx**2+dy**2
    resultado=math.sqrt(dalcuadrado)
    return resultado

print (Distancia (1,2,3,4))