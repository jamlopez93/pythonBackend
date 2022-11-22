from flask import Blueprint
from flask import request

from controllers.candidatos_controller import CandidatosController

candidatos_blueprints = Blueprint('candidatos_blueprints', __name__)
candidatos_controller = CandidatosController()


@candidatos_blueprints.route("/candidatos/<string:id_>", methods=['GET'])
def get_candidatos_by_id(id_):
    response = candidatos_controller.mostrar(id_)
    return response, 200


@candidatos_blueprints.route("/candidatos/insert", methods=['POST'])
def post_candidatos():
    candidatos = request.get_json()
    response = candidatos_controller.crear(candidatos)
    return response, 201


@candidatos_blueprints.route("/candidatos/update/<string:id_>", methods=['PATCH'])
def update_candidatos(id_):
    candidatos = request.get_json()
    response = candidatos_controller.actualizar(id_, candidatos)
    return response, 201


@candidatos_blueprints.route("/candidatos/delete/<string:id_>", methods=['DELETE'])
def delete_candidatos(id_):
    response = candidatos_controller.eliminar(id_)
    return response, 204
