
# Aplicacion del MRO 

# para este caso se ejecuta la funcion hablar directamente de la clase D ya que
# es la primera en la MRO

class A():
    def hablar(self):
        print("Heredado de la clase A")

class B(A):
    def hablar(self):
        print("Heredado de la clase B")

class C(B):
    def hablar(self):
        print("Heredado de la clase C")

class D(B, A):
    def hablar(self):
        print("Original de la clase D")

d = D()
d.hablar() 

# para este caso se ejecuta la funcion hablar de la clase B debido a que cuando se heredan los atributos
# para la clase D, la clase B es la primera en heredarse, despues esta la clase A

class A():
    def hablar(self):
        print("Heredado de la clase A")

class B(A):
    def hablar(self):
        print("Heredado de la clase B")

class C(B):
    def hablar(self):
        print("Heredado de la clase C")

class D(B, A):
    pass

d = D()
d.hablar() 

# Ahora que todas las clases excepto la clase A tienen un pass se hereda el metodo hablar de la
# clase A, la  clase C no se tiene en cuenta debido a que no se hereda a la clase D

class A():
    def hablar(self):
        print("Heredado de la clase A")

class B(A):
    pass

class C(B):
    def hablar(self):
        print("Heredado de la clase C")

class D(B, A):
    pass

d = D()
d.hablar() 

print(D.mro()) #con esta funcion se muestra el orden de ejecucion de el metodo la clase D