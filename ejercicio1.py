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
        return self.sueldo*0.87 # 13% de descuento
        

    def saludar(self):
        print(f'Hola,me llamo {self.nombre} y Tengo {self.edad} años')
