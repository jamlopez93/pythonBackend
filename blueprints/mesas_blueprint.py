from flask import Blueprint
from flask import request

from controllers.mesas_controller import MesasController

mesas_blueprints = Blueprint('mesas_blueprints', __name__)
mesas_controller = MesasController()


@mesas_blueprints.route("/mesas/all", methods=['GET'])
def get_all_mesas():
    response = mesas_blueprints.indice()
    return response, 200


@mesas_blueprints.route("/mesas/<string:id_>", methods=['GET'])
def get_mesa_by_id(id_):
    response = mesas_blueprints.mostrar(id_)
    return response, 200


@mesas_blueprints.route("/mesas/insert", methods=['POST'])
def post_mesas():
    mesas = request.get_json()
    response = mesas_blueprints.crear(mesas)
    return response, 201


@mesas_blueprints.route("/mesas/update/<string:id_>", methods=['PATCH'])
def update_mesas(id_):
    mesas = request.get_json()
    response = mesas_blueprints.actualizar(id_, mesas)
    return response, 201


@mesas_blueprints.route("/mesas/delete/<string:id_>", methods=['DELETE'])
def delete_mesas(id_):
    response = mesas_blueprints.eliminar(id_)
    return response, 204


