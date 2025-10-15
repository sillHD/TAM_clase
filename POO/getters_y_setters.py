# los getters se  usan para accerder a los atributos y metodos encapsulados y los setters se usan para cambiar los valores de esos atributos

class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self.__edad = edad

    # cuando el objeto es muy privado se usa un getter para acceder a el
    def   get_edad(self):
        return self.__edad
        
persona = Persona("lucas",21)

print(persona._nombre)
print(persona.get_edad())