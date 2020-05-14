''' Realizar un programa que conste de una clase llamada Alumno que tenga
como atributos el nombre y la nota del alumno. Definir los métodos para
inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de
la nota y si ha aprobado o no. ́'''
class Alumno():
    def inicializar (self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
    
    def imprimir(self):
        if self.nota==7 or self.nota>7:
            print ('el alumno %s con la nota %s esta aprobado'%(self.nombre,self.nota))
        else:
            print ('el alumno %s con la nota %s esta desaprobado'%(self.nombre,self.nota))

alumno1=Alumno()
alumno1.inicializar(input('ingrese nombre:  '),int(input('ingrese la nota:  ')))
alumno1.imprimir()