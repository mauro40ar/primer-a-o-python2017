'''
 Implementaremos una clase llamada Persona que tendrá como atributo
(variable) el nombre de la persona y dos métodos (funciones). El primero de los
métodos inicializará el atributo nombre y el segundo mostrará por pantalla el
contenido del mismo. Definir dos instancias (objetos) de la clase Persona.
'''

class Personas():
    def __init__(self, nombre):
        self.nombre=nombre
    def setNombre(self):
        self.nombre=nombre  
    def getNombre(self):
        return self.nombre
    def imprimir(self):
        print('el nombre de la persona es %s'%(self.nombre))

person=Personas('miriam')
person1=Personas('azul')
person.imprimir()
person1.imprimir()