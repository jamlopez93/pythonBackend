from flask import Blueprint
from flask import request

from controllers.partidos_controllers import PartidosController

partidos_blueprints = Blueprint('partidos_blueprints', __name__)
partidos_controller = PartidosController()


@partidos_blueprints.route("/partidos/all", methods=['GET'])
def get_all_partidos():
    response = partidos_controller.indice()
    return response, 200


@partidos_blueprints.route("/partidos/<string:id_>", methods=['GET'])
def get_partido_by_id(id_):
    response = partidos_controller.mostrar(id_)
    return response, 200


@partidos_blueprints.route("/partidos/insert", methods=['POST'])
def post_partidos():
    partido = request.get_json()
    response = partidos_controller.crear(partido)
    return response, 201


@partidos_blueprints.route("/partidos/update/<string:id_>", methods=['PATCH'])
def update_partidos(id_):
    partido = request.get_json()
    response = partidos_controller.actualizar(id_, partido)
    return response, 201


@partidos_blueprints.route("/partidos/delete/<string:id_>", methods=['DELETE'])
def delete_partidos(id_):
    response = partidos_controller.eliminar(id_)
    return response, 204


@partidos_blueprints.route("/partidos/<string:nombre_>/canditato/<string:id_>", methods=['GET'])
def consult_partidos(nombre_, id_):
    response = partidos_controller.consulta(nombre_, id_)
    return response, 200
