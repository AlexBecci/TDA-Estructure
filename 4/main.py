# Función para cargar la matriz 3x3 con datos ingresados por el usuario
def cargar_matriz():
    matriz = []
    print("Ingrese los elementos de la matriz 3x3:")
    for i in range(3):
        fila = []
        for j in range(3):
            while True:
                try:
                    valor = int(input(f"Ingrese un número entero para la posición [{i},{j}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Error: Debe ingresar un número entero.")
        matriz.append(fila)
    return matriz

# Función para mostrar la matriz de manera clara
def mostrar_matriz(matriz):
    print("\nMatriz ingresada:")
    for fila in matriz:
        print("   ".join(map(str, fila)))

# Función para calcular la sumatoria de los números pares en la diagonal principal
def suma_pares_diagonal_principal(matriz):
    suma_pares = 0
    for i in range(3):
        if matriz[i][i] % 2 == 0:  # Verificar si el número es par
            suma_pares += matriz[i][i]
    return suma_pares

# Función para calcular la sumatoria de los números impares en la contradiagonal
def suma_impares_contradiagonal(matriz):
    suma_impares = 0
    for i in range(3):
        if matriz[i][2 - i] % 2 != 0:  # Verificar si el número es impar
            suma_impares += matriz[i][2 - i]
    return suma_impares

# Función principal que ejecuta el programa
def main():
    matriz = cargar_matriz()  # Cargar la matriz
    mostrar_matriz(matriz)  # Mostrar la matriz

    # Calcular sumatorias
    suma_pares = suma_pares_diagonal_principal(matriz)
    suma_impares = suma_impares_contradiagonal(matriz)

    # Calcular y mostrar el resultado de la operación
    resultado = suma_pares - suma_impares
    print(f"\nSumatoria de números pares en la diagonal principal: {suma_pares}")
    print(f"Sumatoria de números impares en la contradiagonal: {suma_impares}")
    print(f"Resultado de la operación (pares - impares): {resultado}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
