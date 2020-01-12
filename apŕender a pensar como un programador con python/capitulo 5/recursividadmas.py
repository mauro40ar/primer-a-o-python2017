def factorial(n):
    if n==0:
        return 1
    else:
        rec=factorial(n-1)
        resultado=n*rec
        return resultado
print (factorial(6))
# la recursiva en este caso la primera vez el valor es 3  le resta 1 en el segundo caso el valor es 2 y le resta, en el tercer caso el valor es 1 y le resta, en el cuarto caso es cero y le pone como resultado 1 , luego el 1 se multiplica con el 1 , en el siguiente caso el resultado de la multiplicacion anterior  se multiplica por 2 y el resultado de este se multiplica por 3 dando el resultado final que es 6