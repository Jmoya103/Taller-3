#función que reciba un arreglo de números enteros y retorne un nuevo arreglo con solo los números pares.
#función que reciba un arreglo de números enteros y retorne un nuevo arreglo con solo los números impares.
def LArreglo():
    numArreglo = int(input("Por favor ingrese la cantidad de números de la lista: \t"))
    arreglo = [0] * numArreglo
    for i in range(len(arreglo)):
        valor = int(input("Ingrese el número deseado: \t"))
        arreglo[i] = valor
    return arreglo

def ParArreglo(arreglo):
    Pares = []  #Lista vacia
    for numero in arreglo:
        if (numero%2==0):
            Pares.append(numero) #si el numero cumple la condicion esta funcion almacena en la lista Pares
    return Pares

def ImParArreglo(arreglo):
    ImPares = []  #Lista vacia
    for numero in arreglo:
        if (numero%2!=0):
            ImPares.append(numero) #si el numero cumple la condicion esta funcion almacena en la lista Impares
    return ImPares

def imprimirArreglo(arreglo):
    for num in arreglo:
        print(num, end=" ")
    print()

# Imprimir
arreglo = LArreglo()
print("Arreglo original:")
imprimirArreglo(arreglo)
arreglo_par = ParArreglo(arreglo)
print("Pares del Arreglo son:")
imprimirArreglo(arreglo_par)
arreglo_impar = ImParArreglo(arreglo)
print("Impares del Arreglo son:")
imprimirArreglo(arreglo_impar)
