# Librerias

import random  as rd

# Valores iniciales

marcas = ["Apple","Samsung","Xiaomi","Huawei","Oppo","Vivo","Realme","OnePlus","Sony","Motorola"]
years = [2025,2024,2023,2022,2021,2020,2019,2018]
RAMs = ["2GB","4GB","6GB","8GB"]
camaras = ["8MP","12MP","16MP","24MP","32MP","54MP"]
celulares  = []

# Definicion de la clase y sus atributos
class Celular_Nuevo():
    def __init__(self,clase,marca,year,RAM,camara):
        self.clase = clase
        self.marca =  marca
        self.year = year
        self.RAM = RAM
        self.camara = camara
    
    def caracteristicas(self,i):
        print(f"\n\nCelular #{i} Vendido\n\n")
        print(f"clase: {celular.clase}\nmarca: {celular.marca}\naño:{celular.year}\nRAM: {celular.RAM}\ncamara: {celular.camara}")

class Celular_Viejo(Celular_Nuevo):
    def __init__(self,clase,marca,year,RAM,camara):
        super().__init__(clase,marca,year,RAM,camara)

# Armamos una lista con 100 celulares de ejemplo que fueron vendidos
for i in range(100):
    celulares.append(Celular_Nuevo("Gama Alta",rd.choice(marcas),rd.choice(years),rd.choice(RAMs),rd.choice(camaras)))

for i in range(100):
    celulares.append(Celular_Viejo("Gama Baja",rd.choice(marcas),rd.choice(years),rd.choice(RAMs),"sin camara"))

rd.shuffle(celulares)

i =  1
for celular in celulares:
    celular.caracteristicas(i)

    if i%10 == 0:
        control = input("Desea continuar con los siguientes 10 celulares? (Y/N)\n")
        if control == "N":
            break
    i += 1

print("PROGRAMA FINALIZADO")