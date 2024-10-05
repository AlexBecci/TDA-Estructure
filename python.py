class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f'Hola,me llamo {self.nombre} y Tengo {self.edad} años')


# creando unobjeto de tipo persona

persona1 = Persona('Alex', 22)
persona2 = Persona('Goten', 44)

# Lista que conntiene objetos de tipo persona
lista_personas = [persona1, persona2]

#iterar sobre la lista y usar metodos del TDA

for persona in lista_personas:
    persona.saludar()
