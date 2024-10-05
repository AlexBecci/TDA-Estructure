""" Desarrolla un programa en Python que permita gestionar un sistema de empleados utilizando una estructura de tipo TDA (Tipo de Dato Abstracto). El programa debe permitir cargar, visualizar, buscar, ordenar, actualizar y eliminar empleados. Los empleados deben ser representados mediante una clase que contenga los siguientes atributos:
idLegajo: Número de legajo único de cada empleado.
nombre: Nombre del empleado.
apellido: Apellido del empleado.
edad (opcional).
sueldo: Sueldo bruto del empleado.
Funcionalidades:
Carga de empleados: Permitir al usuario ingresar hasta un máximo de empleados especificado al inicio del programa, con la posibilidad de ingresar menos empleados si lo desea. Debe validar que el sueldo sea un número positivo y generar automáticamente el número de legajo de cada empleado.
Mostrar sueldo neto: Para cada empleado, calcular el sueldo neto aplicando un 13% de descuento sobre el sueldo bruto.
Promedio de sueldos: Calcular y mostrar el promedio de los sueldos de todos los empleados ingresados.
Mejor sueldo: Mostrar el nombre y apellido del empleado con el sueldo más alto.
Mostrar todos los empleados: Listar todos los empleados, mostrando su legajo, nombre, apellido, y sueldo.
Búsqueda de empleado: Permitir buscar un empleado por su número de legajo, utilizando búsqueda binaria si la lista está ordenada.
Ordenar empleados por sueldo: Ordenar la lista de empleados en base al sueldo neto utilizando el método de ordenamiento burbuja.
Eliminar empleado: Permitir eliminar un empleado de la lista basado en su número de legajo.
Actualizar datos del empleado: Permitir modificar el nombre de un empleado dado su número de legajo.
Salir del programa: Finalizar el programa.
Requisitos adicionales:
Debe utilizarse una lista para almacenar los objetos empleados.
El programa debe manejar las excepciones correspondientes cuando el usuario ingrese datos incorrectos (como sueldos negativos o caracteres en lugar de números).
La lista de empleados debe estar ordenada por legajo en todo momento, y debe realizarse una búsqueda binaria para mejorar la eficiencia de la búsqueda de empleados.

 """

# estructura tipo TDA
# Clase


class Empleado:
    def __init__(self, idLegajo, nombre, apellido, sueldo, edad=None):
        self.idLegajo = idLegajo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sueldo = sueldo

    def sueldo_neto(self):
        return self.sueldo*0.87  # 13% de descuento

    # toString
    def __str__(self) -> str:
        return f"Legajo : {self.idLegajo}, Nombre: {self.nombre} , Apellido: {self.apellido}, Sueldo:{self.sueldo}, Sueldo Neto:{self.sueldo_neto():.2f}"

    # saludo
    def saludar(self):
        print(f'Hola,me llamo {self.nombre} y Tengo {self.edad} años')


# funciones del programa
empleados = []
max_empleados = 5  # maximo de empoleados que el usuario puede ingresar
proximo_legajo = 1  # Generacion automatica del numero de legajo idLegajo

# funcion para agregar empleado


def cargar_empleado():
    global proximo_legajo
    while len(empleados) < max_empleados:
        nombre = input("Ingrese el nombre del empleado: ")
        apellido = input("Ingrese el apellido del empleado: ")
        try:
            sueldo = float(input("Ingrese el sueldo bruto del empleado: "))
            if sueldo < 0:
                raise ValueError('EL sueldo no puede ser negativo')
        except ValueError as error:
            print(error)
            continue

        edad = input("Ingrese la edad del empleado (opcional): ")
        edad = int(edad) if edad.isdigit() else None

        empleado = Empleado(proximo_legajo, nombre, apellido, sueldo, edad)
        empleados.append(empleado)

        proximo_legajo += 1
        print('Empleado agregado correctamente')

        if len(empleados) < max_empleados:
            continuar = input('¿Desea ingresar otro empleado? (s/n): ')
            if continuar.lower() != 's':
                break

# mostrar todos los empleados


def mostrar_empleados():
    if not empleados:
        print('No hay empleados registrados')
    else:
        for empleado in empleados:
            print(empleado)

# Función para calcular y mostrar el promedio de los sueldos


def promedio_sueldos():
    if len(empleados) == 0:  # verigicar si la lista esta vacia
        print('No hay empleados registrados')
        return

    total_sueldos = 0  # inicializamos el total sueldos en 0
    for empleado in empleados:
        total_sueldos += empleado.sueldo  # sumar sueldo de cada empleado

    cantidad_empleados = len(empleados)  # obtener cantidad de empleados
    promedio = total_sueldos/cantidad_empleados  # calcular promedio
    print(f'El promedio de sueldo es: {promedio:.2f}')  # imprimir promedio

# Función que busca y muestra el empleado con el mejor sueldo


def mejor_sueldo():
    # Si la lista de empleados esta vacia, mostrar mensaje y terminado
    if len(empleados) == 0:
        print('No hay empleados registrados')
        return
    # inizializar el primer empleado como el empleado con el mejor sueldo por ahora
    empleado_mejor_sueldo = empleados[0]

    # recorrer lista
    for empleado in empleados:
        # comparar el sueldo del epmpeladoactual con el del empleado con el mejor sueldo
        if empleado.sueldo > empleado_mejor_sueldo.sueldo:
            empleado_mejor_sueldo = empleado  # actualizar el empleado con mejor sueldo
    # imprimir resultado

    print(f'El empleado con mejor sueldo ees: {empleado_mejor_sueldo.nombre} {
          empleado_mejor_sueldo.apellido} con un sueldo de {empleado_mejor_sueldo.sueldo:.2f}')


# Función que ordena a los empleados según su sueldo neto utilizando el algoritmo de burbuja

def ordenar_por_sueldo():
    n = len(empleados)  # Obtener el número de empleados
    # Bucle externo para cada pasada de la burbuja
    for i in range(n):
        # Bucle interno para comparar pares de empleados consecutivos
        for j in range(0, n - i - 1):
            # Comparar los sueldos netos de dos empleados consecutivos
            if empleados[j].sueldo_neto() > empleados[j + 1].sueldo_neto():
                # Si están en el orden incorrecto, intercambiarlos
                empleados[j], empleados[j + 1] = empleados[j + 1], empleados[j]

    # Después de la ordenación, mostrar un mensaje
    print("Empleados ordenados por sueldo neto.")

# Función que busca a un empleado por su número de legajo utilizando el algoritmo de búsqueda binaria


def buscar_empleado_por_legajo(legajo):
    inicio = 0  # Índice inicial de la búsqueda
    fin = len(empleados) - 1  # Índice final de la búsqueda

    # Mientras el rango de búsqueda sea válido
    while inicio <= fin:
        medio = (inicio + fin) // 2  # Encontrar el índice medio

        # Si el empleado en la posición media tiene el legajo buscado, devolverlo
        if empleados[medio].idLegajo == legajo:
            return empleados[medio]

        # Si el legajo buscado es mayor que el del empleado en la posición media, buscar en la mitad superior
        elif empleados[medio].idLegajo < legajo:
            inicio = medio + 1

        # Si el legajo buscado es menor, buscar en la mitad inferior
        else:
            fin = medio - 1

    # Si no se encuentra el empleado, devolver None
    return None

# Función que elimina un empleado de la lista basado en su número de legajo


def eliminar_empleado():
    # Pedir al usuario que ingrese el número de legajo
    legajo = int(
        input("Ingrese el número de legajo del empleado que desea eliminar: "))

    # Buscar al empleado con ese legajo
    empleado = buscar_empleado_por_legajo(legajo)

    # Si el empleado se encuentra, eliminarlo de la lista
    if empleado:
        empleados.remove(empleado)  # Eliminar al empleado de la lista
        print("Empleado eliminado correctamente.")
    else:
        # Si no se encuentra, mostrar mensaje de error
        print("Empleado no encontrado.")


# Función que permite actualizar el nombre de un empleado dado su número de legajo
def actualizar_empleado():
    # Pedir al usuario que ingrese el número de legajo
    legajo = int(
        input("Ingrese el número de legajo del empleado que desea actualizar: "))

    # Buscar al empleado con ese legajo
    empleado = buscar_empleado_por_legajo(legajo)

    # Si el empleado se encuentra, pedir el nuevo nombre y actualizarlo
    if empleado:
        # Pedir el nuevo nombre
        nuevo_nombre = input("Ingrese el nuevo nombre del empleado: ")
        empleado.nombre = nuevo_nombre  # Actualizar el nombre del empleado
        print("Empleado actualizado correctamente.")
    else:
        # Si no se encuentra, mostrar mensaje de error
        print("Empleado no encontrado.")
