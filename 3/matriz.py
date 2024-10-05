import random

# Función para inicializar la matriz 3x3


def inicializar_matriz():
    matriz = [[0 for _ in range(3)] for _ in range(3)]
    return matriz

# Función para cargar los elementos manualmente (excepto la diagonal principal)


# Función para cargar los elementos manualmente (excepto la diagonal principal)
def cargar_matriz(matriz):
    for i in range(3):
        for j in range(3):
            if i == j:
                matriz[i][j] = random.randint(1, 10)  # Cargar la diagonal principal con números aleatorios
            else:
                while True:
                    try:
                        valor = int(input(f"Ingrese un número entero para la posición [{i},{j}]: "))
                        matriz[i][j] = valor
                        break
                    except ValueError:
                        print("Error: Debe ingresar un número entero.")
    return matriz  # Mover el return fuera del bucle para que la función termine al final


def calcular_promedios(matriz):
    pares = []
    impares = []

    # Recorremos la matriz para separar números pares e impares
    for i in range(3):
        for j in range(3):
            numero = matriz[i][j]
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)

    # Calcular la suma manualmente
    suma_pares = 0
    suma_impares = 0
    for par in pares:
        suma_pares += par
    for impar in impares:
        suma_impares += impar

    # Calcular el promedio manualmente
    cantidad_pares = 0
    for _ in pares:
        cantidad_pares += 1

    cantidad_impares = 0
    for _ in impares:
        cantidad_impares += 1

    promedio_pares = suma_pares / cantidad_pares if cantidad_pares > 0 else 0
    promedio_impares = suma_impares / cantidad_impares if cantidad_impares > 0 else 0

    return promedio_pares, promedio_impares

# Función para mostrar la matriz


def mostrar_matriz(matriz):
    print("\nMatriz generada:")
    for fila in matriz:
        print(fila)

# Menú principal


def menu():
    matriz = inicializar_matriz()

    while True:
        print("\n----- Menú de Gestión de Matriz 3x3 -----")
        print("1. Inicializar y cargar matriz")
        print("2. Mostrar matriz")
        print("3. Calcular promedios de números pares e impares")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            matriz = cargar_matriz(matriz)
            print("Matriz cargada exitosamente.")
        elif opcion == "2":
            mostrar_matriz(matriz)
        elif opcion == "3":
            promedio_pares, promedio_impares = calcular_promedios(matriz)
            print(f"\nPromedio de números pares: {promedio_pares:.2f}")
            print(f"Promedio de números impares: {promedio_impares:.2f}")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


# Llamar al menú principal
menu()
