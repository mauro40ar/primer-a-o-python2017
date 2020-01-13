def factorial(n):
    if type(n)!=type(1):
        print("el factorialesta definido solo para enteros.")
        return -1            #guardian una condicion que comprueba y maneja circunstancias que pudieran provocar un error
    elif n<0:
        print("el factorial esta definido solo para enteros \ positivos")
        return -1
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
print (factorial(-15))
print (factorial("hola"))
print (factorial(15))