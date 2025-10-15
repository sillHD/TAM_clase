class Persona:  # (Clase Padre o Superclase)
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad


class Estudiante:  # Clase Estudiante independiente
    def __init__(self, nombre, colegio, grado):
        self.nombre = nombre
        self.colegio = colegio
        self.grado = grado

    def datos(self):
        print(f"""DATOS DEL ESTUDIANTE\n
        Nombre: {self.nombre}
        Colegio: {self.colegio}
        Grado: {self.grado}""")


# Ejemplo Herencia simple
class Empleado(Persona):  # Herencia de Persona a Empleado
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario



# Ejemplo Herencia múltiple 
class PersonaYEstudiante(Persona, Estudiante):
    def __init__(self, nombre, edad, nacionalidad, colegio, grado):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Estudiante.__init__(self, nombre, colegio, grado)

    def datos1(self):
        super().datos()

# Crear un objeto de PersonaYEstudiante
estudiante1 = PersonaYEstudiante("Alfredo", 19, "Mexicana", "Ninguno", "No aplica")
estudiante1.datos1()
