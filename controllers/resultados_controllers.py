from models.resultados import Resultados


class ResultadosController:

    # Constructor
    def __init__(self):
        print("controlador de Resultados")

    # Mostrar todos los Resultados por candidato y partido todas las mesas, metodo GET
    def indice(self, candidatoid_: str) -> list:
        print("GETAll")
        data = {
            "votos": "250",
            "_idcandidato": candidatoid_,
            "partido": "partido x"
        }
        return [data]

    # Mostrar todos los Resultados por candidato y partido mesa especifica, metodo GET
    def votopormesacandidato(self, candidatoid_: str, id_: str) -> list:
        print("GETAll")
        data = {
            "votos": "250",
            "_idcandidato": candidatoid_,
            "_id": id_,
            "partido": "partido x"
        }
        return [data]

    # Mostrar todos los Resultados por mesa especifica, metodo GET
    def votopormesa(self, id_: str) -> list:
        print("GETAll")
        data = {
            "votos": "250",
            "_id": id_,

        }
        return [data]
