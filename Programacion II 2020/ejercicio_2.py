''' Declarar una segunda clase llama Empleado que hereda de la clase Persona y
agrega el atributo sueldo. Debe mostrar si tiene que pagar impuestos o no
(sueldo superior a 3000). Crear un objeto de cada clase '''
class Persona():
    def inicializar(self,nombre):
        self.nombre=nombre
    def imprimir(self):
        return self.nombre

class Empleado(Persona):
    def inicializar(self,sueldo):
        self.sueldo=Sueldo 
    
    def pagarAtributo(self):
        self.sueldo=int(input('ingrese sueldo: '))
        if self.sueldo<3000:
            print ('no paga impuesto')
        else:
            print ('debe pagar impuesto')

persona1=Persona() 
persona1.inicializar(input('ingrese nombre: '))
persona1.imprimir()

empleado1=Empleado()
empleado1.pagarAtributo()
'''
