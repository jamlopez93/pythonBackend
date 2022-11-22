from models.mesas import Mesas


class MesasController:

    # Constructor
    def __init__(self):
        print("controlador de partidos")

    # Mostrar todas las mesas, metodo GET
    def indice(self) -> list:
        print("GETAll")
        data = {
            "numero_mesa": "dsfd2324",
            "numero cedulas": "200"
        }
        return [data]

    # Mostrar una sola mesa, metodo GET
    def mostrar(self, numero_mesa_: str) -> dict:
        print("Un partido")
        data = {
            "numero_mesa": numero_mesa_,
            "numero cedulas": "200"
        }
        return data

    # Crear una mesa, metodo POST
    def crear(self, mesa_: dict) -> dict:
        print("Crear")
        mesa = Mesas(mesa_)
        return mesa.__dict__

    # Actualizar cedulas, metodo PATCH
    def actualizar(self, id_: str,  mesa_: dict):
        print("Actualizar")
        data = mesa_
        data['_id'] = id_
        partido = Mesas(mesa_)
        return partido.__dict__

    # Eliminar un partido, metodo DELETE
    def eliminar(self, id_: str):
        print("Eliminado " + id_)
        return {"Delete count": 1}


