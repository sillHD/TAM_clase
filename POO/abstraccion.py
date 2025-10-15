class celular():
    def __init__(self):
        self._estado = "apagado"
    
    def encender(self):
        self._estado = "encendido"
        print("el celular esta encendido")

    def iniciar(self):
        if self._estado == "apagado":
            self._estado = "encendido"
        print("inicializando el celular")

Cel = celular()
Cel.iniciar()