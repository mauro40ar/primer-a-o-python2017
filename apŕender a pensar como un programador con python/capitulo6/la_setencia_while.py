def cuenta_atras(n):
    while n>0:
        print (n)
        n=n-1
    print ("buen viaje")
cuenta_atras(5)

def secuencia(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n=n/2
        else:
            n=n*3+1
secuencia(20)