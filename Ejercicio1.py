#Ejercicio 1: Suma de los elementos de un arreglo
#Descripción: Crea una función que reciba un arreglo de enteros y retorne la suma de todos sus elementos.
#Debe tener la función para crear el arreglo e imprimirlo.
#No se pueden usar funciones propias de listas
def crearArreglo (tamanoArreglo):
    j=True
    while j:
        if tamanoArreglo < 0 :
            print("El tamaño del arreglo debe ser mayor a 0, vuelva a ingresar los datos ")
        if tamanoArreglo > 0:
            arreglo = [0]*tamanoArreglo
            j=False
            return arreglo
def pedirDatosArreglo (arreglo):
    for i in range(len(arreglo)):
        datosarreglo= int(input(f"Ingrese el dato {i} dek arreglo: "))
        arreglo[i] = datosarreglo
    return arreglo

def sumarDatosArreglo (arreglo):
    sumatotal=0
    for i in range(len(arreglo)):
        sumatotal = arreglo[i] +sumatotal
    return sumatotal

longitudarreglo= int(input("Ingrese el tamaño del arreglo: "))
arreglovacio= crearArreglo(longitudarreglo)
arreglocondatos = pedirDatosArreglo(arreglovacio)
resultadoSuma = sumarDatosArreglo(arreglocondatos)
print(f"El arreglo resultante es {arreglocondatos}")
print(f"El resultado de la suma es: {resultadoSuma}")




