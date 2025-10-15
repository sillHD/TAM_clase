# PRIMERA PARTE

class Persona():
    def __init__(self,nombre,edad): # Definicion de los atributos
        self.nombre = nombre
        self.edad = edad

    def Datos(self):
        print(f"""DATOS:\n\nnombre: {self.nombre}\nedad: {self.edad}""")

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
    
    def Datos_grado(self):
        print(f"grado:{self.grado}")

estudiante = Estudiante("julio","19","noveno")
estudiante.Datos()
estudiante.Datos_grado()

# SEGUNDA PARTE

class Animal():
    def comer(self):
        print("el animal esta comiendo")\
        
class Mamifero(Animal):
    def amamantar(self):
        print("el animal esta amamantando")

class Ave(Animal):
    def volar(self):
        print("el animal esta volando")

class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago()
murcielago.comer()
murcielago.amamantar()
murcielago.volar()