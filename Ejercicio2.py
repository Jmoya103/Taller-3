def crear_matriz(filas, columnas):
    print(f"Introduce los elementos de la matriz de {filas} x {columnas}:")
    matriz = [[int(input(f"Ingrese el número en la posición ({i+1},{j+1}): ")) for j in range(filas)] for i in range(columnas)]
    return matriz

def encontrarMax(matriz):
    numeroMax = int()
    for fila in matriz:
        for num in fila:
            if num > numeroMax:
                numeroMax = num 
    return numeroMax

def encontrarMin(matriz):
    numeroMin = matriz[0][0]
    for fila in matriz:
        for num in fila:
            if num < numeroMin:
                numeroMin = num
    return numeroMin

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

filas= int(input("Ingrese el número de filas de la matriz: "))
columnas= int(input("Ingrese el número de columnas de la matriz: "))

matriz = crear_matriz(filas, columnas)

print("Matriz generada:")
imprimir_matriz(matriz)

maxNum = encontrarMax(matriz)
minNum = encontrarMin(matriz)

print("El número más grande es:", maxNum)
print("El número más pequeño es:", minNum)
