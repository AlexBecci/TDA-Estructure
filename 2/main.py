# Importar funciones desde alumnos.py
from alumnos import cargar_alumnos, mostrar_alumnos, calcular_promedio, mostrar_bajo_promedio, alumnos

def menu():
    while True:
        print("\n----- Menú de Gestión de Alumnos -----")
        print("1. Cargar alumno")
        print("2. Mostrar todos los alumnos")
        print("3. Calcular promedio de notas")
        print("4. Mostrar alumnos con nota por debajo del promedio")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_alumnos()  # Llamar a la función cargar_alumnos
        elif opcion == "2":
            mostrar_alumnos()  # Llamar a la función mostrar_alumnos
        elif opcion == "3":
            if alumnos:
                promedio = calcular_promedio(alumnos)  # Calcular el promedio de los alumnos
                print(f"Promedio de notas: {promedio:.2f}")
            else:
                print("No hay alumnos registrados para calcular el promedio.")
        elif opcion == "4":
            if alumnos:
                promedio = calcular_promedio(alumnos)  # Calcular el promedio de los alumnos
                mostrar_bajo_promedio(alumnos, promedio)  # Mostrar los alumnos con nota por debajo del promedio
            else:
                print("No hay alumnos registrados.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Llamar al menú principal
menu()
