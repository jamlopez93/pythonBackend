from Repositorios.InterfazRepositorio import InterfazRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId


class ResultadoRepositorio(InterfazRepositorio[Resultado]):

    def getListadoCandidatosInscritosMesa(self, id_mesa):
        """
        Genera votaciones por mesa
        :param id_mesa: Número de identificación de la mesa
        :return: lista de votaciones por mesa
        """
        theQuery = {"mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)

    def getListadoMesasCandidatoInscrito(self, id_candidato):
        """
        Retorna las votaciones por candidato
        :param id_candidato: Número de identificación del candidato
        :return: Lista de votaciones por candidato
        """
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)


    def getNumeroCedulaMayorCandidato(self):
        """
        Numero de votos mayor de candidato por cédula
        :return:
        """
        query = {
            "$group":{
                "_id": "$candidato",
                "Total_votaciones_por_id": {
                    "$sum": 1
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query]
        return self.queryAggregation(pipeline)
