import random
marca = ("apple","motorola","samsung","xiaomi")
modelo = ("2023","2020","2005","2006")
camara = ('48MP','50MP','32MP','5MP')
celulares = [] 
class celular():
    # funcion constructora o metodo constructor, crea los atributos de instancia
    def __init__(self,marca,modelo,camara): 
        # definicion de los atributos
        self.marca = marca 
        self.modelo = modelo
        self.camara = camara

for i in range(len(marca)):
    # establecemos los atributos con las listas y lo agregamos a otra lista
    celular1 =  celular(random.choice(marca),random.choice(modelo),random.choice(camara))
    celulares.append(celular1)

for i in range(len(marca)):
    # printeamos los objetos
    print(f"CELULAR {i+1}\nmarca = {celulares[i].marca}\nmodelo = {celulares[i].modelo}\ncamara = {celulares[i].camara}\n\n")