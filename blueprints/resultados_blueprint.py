from flask import Blueprint
from flask import request

from controllers.resultados_controllers import ResultadosController

resultados_blueprints = Blueprint('resultados_blueprints', __name__)
resultados_controller = ResultadosController()


@resultados_blueprints.route("/resultados/all", methods=['GET'])
def get_all_resultados(candidatoid_):
    response = resultados_blueprints.indice(candidatoid_)
    return response, 200

@resultados_blueprints.route("/resultados/mesa", methods=['GET'])
def get_votopormesacandidato(candidatoid_, id_):
    response = resultados_blueprints.votopormesacandidato(candidatoid_, id_)
    return response, 200


@resultados_blueprints.route("/resultados/<string:id_>", methods=['GET'])
def get_votopormesa(id_):
    response = resultados_blueprints.votopormesa(id_)
    return response, 200

