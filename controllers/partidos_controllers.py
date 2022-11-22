from models.partidos import Partidos


class PartidosController:

    # Constructor
    def __init__(self):
        print("controlador de partidos")

    # Mostrar todos los partidos, metodo GET
    def indice(self) -> list:
        print("GETAll")
        data = {
            "_id": "dsfd2324",
            "nombre": "partido x",
            "lema": "que robo la tributaria"
        }
        return [data]

    # Mostrar un solo partido, metodo GET
    def mostrar(self, id_: str) -> dict:
        print("Un partido")
        data = {
            "_id": id_,
            "nombre": "partido x",
            "lema": "que robo la tributaria"
        }
        return data

    # Crear un partido, metodo POST
    def crear(self, partido_: dict) -> dict:
        print("Crear")
        partido = Partidos(partido_)
        return partido.__dict__

    # Actualizar informacion de un partido, metodo PATCH
    def actualizar(self, id_: str, partido_: dict):
        print("Actualizar")
        data = partido_
        data['_id'] = id_
        partido = Partidos(partido_)
        return partido.__dict__

    # Eliminar un partido, metodo DELETE
    def eliminar(self, id_: str):
        print("Eliminado " + id_)
        return {"Delete count": 1}

    # Consultar todos los candidatos de un partido, metodo GET
    def consulta(self, nombre_: str, id_: str) -> dict:
        print("consulta del partido")
        data = {
            "nombre_": nombre_,
            "_id": id_
        }
        return data
