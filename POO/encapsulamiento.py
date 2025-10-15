# el encapsulamiento los usamos cuando queremos clasificar  atributos, objetos, o metodos como publicos, privados, y muy privados
# si los establecemos como privados o muy privados no podremos  acceder a ellos a menos  que tengamos permiso 
class comun(): 
    def __init__(self,atributo1,atributo2,atributo3):

        #  Atributo publico
        self.atributo1 = "valor"

        # Atributo Privado 
        self._atributo2 = "valor"

        # Atributo Muy Privado 
        self.__atributo3 =  "valor"

        # Tambien aplica para los metodos

        def _accion(): # Metodo privado
            pass  