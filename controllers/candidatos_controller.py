from models.candidatos import Candidatos


class CandidatosController:

    # Constructor
    def __init__(self):
        print("controlador de partidos")

    # Mostrar un solo Candidato, metodo GET
    def mostrar(self, numero_resolucion_: str) -> dict:
        print("Un Candidato")
        data = {
            numero_resolucion_: "dsfd2324",
            "cedula": "2189428",
            "nombre": "candidato",
            "apellido": "lopez",
            "_idpartido": "dsfd2324"
        }
        return data

    # Crear un candidato, metodo POST
    def crear(self, candidato_: dict) -> dict:
        print("Crear")
        candidato = Candidatos(candidato_)
        return candidato.__dict__

    # Actualizar informacion de un candidato, metodo PATCH
    def actualizar(self, numero_resolucion_: str, candidato_: dict):
        print("Actualizar")
        data = candidato_
        data['_id'] = numero_resolucion_
        candidatos = Candidatos(candidato_)
        return candidatos.__dict__

    # Eliminar un partido, metodo DELETE
    def eliminar(self, numero_resolucion_: str):
        print("Eliminado " + numero_resolucion_)
        return {"Delete count": 1}
