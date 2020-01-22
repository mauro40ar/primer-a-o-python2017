def positivonegativoneutro(n):
    if n>0:
        return "es positivo"
    elif n<0:
        return "es negativo"
    else:
        return "es neutro"
print(positivonegativoneutro(int(input("ingrese numero: "))))