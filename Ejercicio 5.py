
#Descripción: Escribe una función que reciba un arreglo de números enteros y retorne otro arreglo con los elementos en orden inverso.
#Debe tener la función para crear el arreglo e imprimirlo.
#No se pueden usar funciones propias de listas
def LArreglo():
    numArreglo = int(input("Por favor ingrese la cantidad de números de la lista: \t"))
    arreglo = [0] * numArreglo
    for i in range(len(arreglo)):
        valor = int(input("Ingrese el número deseado: \t"))
        arreglo[i] = valor
    return arreglo

def inverArreglo(arreglo):
    inicio = 0
    fin = len(arreglo) - 1 #se resta -1 para que la variable fin cubra el ultimo valor del arreglo
    while inicio < fin:
        # Intercambiar los elementos en las posiciones inicio y fin
        aux = arreglo[inicio]
        arreglo[inicio] = arreglo[fin]
        arreglo[fin] = aux
        # Mover los índices hacia el centro
        inicio += 1
        fin -= 1
    return arreglo

def imprimirArreglo(arreglo):
    for num in arreglo:
        print(num, end=" ")
    print()

# Imprimir
arreglo = LArreglo()
print("Arreglo original:")
imprimirArreglo(arreglo)
arreglo_inverso = inverArreglo(arreglo)
print("Arreglo invertido:")
imprimirArreglo(arreglo_inverso)


