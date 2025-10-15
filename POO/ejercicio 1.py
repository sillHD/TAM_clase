
class estudiante(): # clase
    def __init__(self,nombre,edad,grado): # defincion de los atributos
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self): # definicion del metodo
        print(f"estudiando...") 

estudiante1 = estudiante(input("ingrese el nombre del estudiante:"),input("ingrese la edad del estudiante:"),input("ingrese el grado del estudiante:"))

print(f"""
            Datos del estudiante:\n
          
            NOMBRE: {estudiante1.nombre}
            EDAD: {estudiante1.edad}
            GRADO: {estudiante1.grado}
          """)
while True:
    entrada = input("")
    if entrada.lower() == "estudiar":
        estudiante1.estudiar()




    