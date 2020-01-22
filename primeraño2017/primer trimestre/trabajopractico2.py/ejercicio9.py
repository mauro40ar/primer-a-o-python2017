def vehiculo(n):
    if n==1:
        return "bicicleta"
    elif n==2 and n<3:
        return "moto"
    elif n==4 or n<6:
        return "auto"
    elif n==12 or n<14:
        return "camioneta"
    elif n==40 or n<50:
        return "colectivo"
    else:
        return "tren"    
print(vehiculo(100))