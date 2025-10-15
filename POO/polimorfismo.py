# ejemplo de polimorfismo
class Gato():
    # metodo sonido para la clase Gato
    def sonido(self): 
        return "miau"

class Perro():
    # mismo metodo pero para la  clase Perro
    def sonido(self):
        return "guau"

def hacer_sonido(animal):
    print(animal.sonido())

# Definicion de los objetos
gato = Gato()
perro = Perro()

# en ambos casos se llama un mismo metodo pero que retorna un diferente valor dependiendo del objeto
print(gato.sonido()) 
print(perro.sonido())

# otro  modo de hacer polimorfismo es con otra funcion

hacer_sonido(gato)
hacer_sonido(perro)