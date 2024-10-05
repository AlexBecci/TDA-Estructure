# Clase Alumno
class Alumno:
    def __init__(self, matricula, nombre, curso, nota):
        self.matricula = matricula
        self.nombre = nombre
        self.curso = curso
        self.nota = nota

    def __str__(self):
        return f"{self.nombre} - Matrícula: {self.matricula} - Curso: {self.curso} - Nota: {self.nota}"

# Lista global de alumnos
alumnos = []

# Función para cargar información de los alumnos
def cargar_alumnos(cantidad_alumnos=5):
    for i in range(cantidad_alumnos):
        print(f'\nAlumno {i+1}:')
        matricula = input("Ingrese matrícula: ")
        nombre = input("Ingrese apellido y nombre: ")
        curso = input("Ingrese curso: ")

        # Validación de la nota
        while True:
            try:
                nota = float(input("Ingrese nota (0 a 10): "))
                if 0 <= nota <= 10:
                    break
                else:
                    print('Error: la nota debe ser entre 0 y 10.')
            except ValueError as error:
                print(f'Error: {error}')

        # Crear una instancia de Alumno y agregarla a la lista
        alumnos.append(Alumno(matricula, nombre, curso, nota))

# Función para mostrar todos los alumnos
def mostrar_alumnos():
    if not alumnos:
        print("No hay alumnos registrados.")
    else:
        print("\n--- Lista de Alumnos ---")
        for alumno in alumnos:
            print(alumno)

# Función para calcular el promedio de notas del grupo sin usar sum()
def calcular_promedio(alumnos):
    total_notas = 0  # Inicializar el total de las notas

    # Iterar sobre la lista de alumnos y sumar sus notas
    for alumno in alumnos:
        total_notas += alumno.nota

    # Calcular el promedio dividiendo el total de notas entre el número de alumnos
    promedio = total_notas / len(alumnos) if len(alumnos) > 0 else 0
    return promedio

# Función para mostrar alumnos con nota por debajo del promedio
def mostrar_bajo_promedio(alumnos, promedio):
    print(f"\nPromedio del grupo: {promedio:.2f}")
    print("Alumnos con nota por debajo del promedio:")

    encontrados = False  # Bandera para verificar si se encuentran alumnos debajo del promedio
    for alumno in alumnos:
        if alumno.nota < promedio:
            print(f"- {alumno.nombre} (Nota: {alumno.nota})")
            encontrados = True

    if not encontrados:
        print("Todos los alumnos tienen notas iguales o superiores al promedio.")
