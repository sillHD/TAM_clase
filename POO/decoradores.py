def decorador(funcion):
    def funcion_modificada():
        print("antes de ejecutar la funcion decoradora")
        funcion() #ejecutamos la funcion decoradora
        print("despues de ejecutar la funncion decoradora")
    return funcion_modificada

# def decoradora(): # en este  punto se asigna la funcion decoradora
#     print("Hola mundo")

# saludo_modificado = decorador(decoradora) #para que funncione el codigo se tiene que realizar este cambio, pero tambien se puede realizar lo siguiente
# saludo_modificado()

@decorador # el @ es la palabra reservada para el decorador
def saludo():
    print("Hola mundo")
saludo()