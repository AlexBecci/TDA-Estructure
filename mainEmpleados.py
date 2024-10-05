# main

# import el modulo de empleados

from empleados import cargar_empleado,mostrar_empleados,promedio_sueldos,mejor_sueldo,ordenar_por_sueldo,buscar_empleado_por_legajo,eliminar_empleado,actualizar_empleado

def menu():
    while True:
        print("\n----- Menú de Gestión de Empleados -----")
        print("1. Cargar empleado")
        print("2. Mostrar todos los empleados")
        print("3. Mostrar promedio de sueldos")
        print("4. Mostrar mejor sueldo")
        print("5. Ordenar empleados por sueldo neto")
        print("6. Buscar empleado por legajo")
        print("7. Eliminar empleado")
        print("8. Actualizar datos del empleado")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_empleado()
        elif opcion == "2":
            mostrar_empleados()
        elif opcion == "3":
            promedio_sueldos()
        elif opcion == "4":
            mejor_sueldo()
        elif opcion == "5":
            ordenar_por_sueldo()
        elif opcion == "6":
            legajo = int(input("Ingrese el número de legajo: "))
            empleado = buscar_empleado_por_legajo(legajo)
            if empleado:
                print(empleado)
            else:
                print("Empleado no encontrado.")
        elif opcion == "7":
            eliminar_empleado()
        elif opcion == "8":
            actualizar_empleado()
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

#llamar menu principal
menu()
