'''. Implementaremos una clase llamada Persona que tendrá como atributo
(variable) el nombre de la persona y dos métodos (funciones). El primero de los
métodos inicializará el atributo nombre y el segundo mostrará por pantalla el
contenido del mismo. Definir dos instancias (objetos) de la clase Persona.'''

class Persona():
    def inicializar (self,nombre):
        self.nombre=nombre
    
    def imprimir(self):
        print (self.nombre)
persona1=Persona() 
persona1.inicializar(input('ingrese nombre: '))
persona1.imprimir()

persona2=Persona() 
persona2.inicializar(input('ingrese nombre: '))
persona2.imprimir()

