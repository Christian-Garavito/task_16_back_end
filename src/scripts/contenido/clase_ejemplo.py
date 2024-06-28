""" Ejemplo clase ejercicio """

class NotFoundArgs(Exception):
    """ Excepcion customizada para informar la falta de parametros """

class ClaseEjemplo:
    """ Clase de ejemplo """
    def __init__(self) -> None:
        self.nombre_pokemon = None
        self.nombre_entrenador = None


    def validar(self, args):
        """ funcion para validar las entradas del controlador """

        if not "nombre_pokemon" in args:
            raise NotFoundArgs("No se ha encontrado el nombre del pokemon en las entradas")
        if not "nombre_entrenador" in args:
            raise NotFoundArgs("No se ha encontrado el nombre del entrenador en las entradas")

        self.nombre_pokemon = args["nombre_pokemon"]
        self.nombre_entrenador = args["nombre_entrenador"]
