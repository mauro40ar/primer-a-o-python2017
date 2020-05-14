''' Realizar un programa que conste de una clase llamada Alumno que tenga
como atributos el nombre y la nota del alumno. Definir los métodos para
inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de
la nota y si ha aprobado o no. ́'''


class Alumno():
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    def setNombre(self):
        self.nombre=nombre
    def setNota(self):
        self.nota=nota
    def getNombre(self):
        return self.nombre
    def getNota(self):
        return self.nota
    def imprimir(self):
        if self.nota>=7:
            print('El alumno %s saco la nota %s y esta aprobado'%(self.nombre,self.nota))
        else:
            print('El alumno %s saco la nota %s y esta desaprobado'%(self.nombre,self.nota))
al=Alumno(input('ingrese nombre: '),int(input('ingrese nota:  ')))
al.imprimir()