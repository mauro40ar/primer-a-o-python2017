def transporte(grey):
    if grey>0 and grey==1:
        print ("bicicleta")
    elif grey==2 or grey<5:
        print ("auto")
    elif grey==5 or grey<=30:
        print ("micro")
    else:
        print ("avion")
transporte()