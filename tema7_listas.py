#listas 

lista1=[10,5,3]
lista2=[1.5,2.66,1.70,89.2]
lista3=["Lunes", "Martes", "Miercoles"]
lista4=["Juan", 45,1.92]


#tuplas
print(type(lista1))
print(len(lista1))



print(lista1[0])

suma=0

x=0
while x < len(lista1):
    suma=suma+lista1[x]
    x=x+1

print("La suma es: {}", format(suma))
print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])


lista5=[]

for x in range(5):
    valor=int(input("Ingresa valor:"))
    lista5.append(valor)


print(lista5)


#eliminar elementos de la lista
print(lista1)
lista1.pop()
print(lista1)



"""

Crear un programa, pedir una cantidad n de numeros y almacenarlos en un arreglo 
la salida debera ser la siguiente:
lista completa: xxxxxxxx
numero pares de la lista: aaaaaaa
numeros impares de la lista 

"""
numeros = []

cantidad = int(input("Ingresa la cantidad de números que desees ingresar: "))

for x in range(cantidad):
    valor = int(input(f"Ingresa valor {x+1}: "))
    numeros.append(valor)

pares = [num for num in numeros if num % 2 == 0] 
impares = [num for num in numeros if num % 2 != 0] 

print("Lista completa: ", numeros)
print("Pares: ", pares)
print("Impares: ", impares)


"""

"""


