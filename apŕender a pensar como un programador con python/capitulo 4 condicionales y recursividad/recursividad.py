def cuenta_atras(n):
    if n>0:
        print("%s"%(n))
        print (cuenta_atras(n-1))
    else:
        print("buen viaje")
n=3       
cuenta_atras(n)