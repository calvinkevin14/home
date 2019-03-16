#!/usr/bin/python

def evaluacion(i):
    resultado="aprobado"
    if 5>i:
        resultado="suspendido"
    return resultado

#print("introduce un numero")
nota_alumno=input("introduce un numero: ")
print(evaluacion(nota_alumno))
