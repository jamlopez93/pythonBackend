
from flask import Flask, request, Response
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from Controladores.PartidoControlador import PartidoControlador
from Controladores.CandidatoControlador import CandidatoControlador
from Controladores.MesaControlador import MesaControlador
from Controladores.ResultadoControlador import ResultadoControlador

app = Flask(__name__)
cors = CORS(app)


#def load_file_config():
    #with open("config.json", "r") as config:
        #data = json.load(config)
    #return data

#if __name__ == '__main__':
    #data_config = load_file_config()
    #print ("Server running: http://" + data_config.get("url-backend")+ ":" + str(data_config.get('port')))
    #serve(app, host= data_config.get('url-backend'), port = data_config.get('port'))


miControladorPartido = PartidoControlador()
miControladorCandidato = CandidatoControlador()
miControladorMesa = MesaControlador()
miControladorResultado = ResultadoControlador()


@app.route("/", methods=["GET"])
def test():
    """
    Probar el servicio
    :return: Mensaje el servidor esta corriendo
    """
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


@app.route("/partidos", methods=["GET"])
def getPartidos():
    """
    endpoint partidos método get
    :return: Partidos
    """
    json = miControladorPartido.index()
    return jsonify(json)


@app.route("/partidos", methods=["POST"])
def crearPartido():
    """
    Creación de partido
    :return: nuevo partido
    """
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=["GET"])
def getPartido(id):
    """
    Muestra partido
    :param id: identificación partidos
    :return: Un partido
    """
    json = miControladorPartido.show(id)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=["PUT"])
def modificarPartido(id):
    """
    Modificar partido
    :param id: identificación partido
    :return: Partido modificado
    """
    data = request.get_json()
    print(data)
    json = miControladorPartido.update(id, data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=["DELETE"])
def eliminarPartido(id):
    """
    Eliminar partido
    :param id: Identificación partido
    :return: Partido eliminado
    """
    json = miControladorPartido.delete(id)
    return jsonify(json)


@app.route("/candidatos", methods = ["GET"])
def getCandidatos():
    """
    Ingresar candidatos
    :return: Candidatos

    """
    json = miControladorCandidato.index()
    return jsonify(json)


@app.route("/candidatos", methods =["POST"])
def crearCandidato():
    """
    Craer candidato
    :return: Candidato Creado
    """
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)


@app.route("/candidatos/<string:id_candidato>", methods = ["GET"])
def getCandidato(id_candidato):
    """
    Mostrar candidato por Id
    :param id_candidato: Identificación candidato
    :return: Candidato por Id
    """
    json = miControladorCandidato.show(id_candidato)
    return jsonify(json)


@app.route("/candidatos/<string:id_candidato>", methods = ["PUT"])
def modificarCandidato(id_candidato):
    """
    Modificar candidato
    :param id_candidato: Identificación candidato
    :return: Candidato modificado
    """
    data = request.get_json()
    json = miControladorCandidato.update(id_candidato, data)
    return jsonify(json)


@app.route("/candidatos/<string:id_candidato>", methods = ["DELETE"])
def eliminarCandidato(id_candidato):
    """
    Eliminar candidato
    :param id_candidato: Identificación candidato
    :return: candidato eliminado
    """
    json = miControladorCandidato.delete(id_candidato)
    return jsonify(json)


@app.route("/candidatos/<string:id_candidato>/partido/<string:id_partido>", methods=["PUT"])
def asignarPartidoCandidato(id_candidato, id_partido):
    """
    Asignar Candidato
    :param id_candidato: Identificación candidato
    :param id_partido: Identificación partido
    :return: Candidato asignado a partido
    """
    json = miControladorCandidato.asignarCandidato(id_candidato, id_partido)
    return jsonify(json)


@app.route("/mesas", methods=["GET"])
def getMesas():
    """
    Ingresar mesas
    :return: mesas nuevas
    """
    json = miControladorMesa.index()
    return jsonify(json)


@app.route("/mesas", methods=["POST"])
def crearMesa():
    """
    Crear datos mesa
    :return: Datos mesa
    """
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=["GET"])
def getMesa(id):
    """
    Mostrar mesaa por Id
    :param id: Identificación
    :return: Mesas por Id
    """
    json = miControladorMesa.show(id)
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=["PUT"])
def modificarMesa(id):
    """
    Modificar mesa
    :param id: Identificación
    :return: Mesa modificada
    """
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=["DELETE"])
def eliminarMesa(id):
    """
    Eliminar mesa
    :param id: Identificación
    :return: Mesa eliminada
    """
    json = miControladorMesa.delete(id)
    return jsonify(json)


@app.route("/resultados", methods = ["GET"])
def getResultados():
    """
    Obtener todos los resultados
    :return: Todos los resultados
    """
    json = miControladorResultado.index()
    return jsonify(json)


@app.route("/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods =["POST"])
def crearResultado(id_mesa, id_candidato):
    """
    Añadir un resultado a una mesa
    :param id_mesa: Identificación mesa
    :param id_candidato: Identificación candidato
    :return: Nuevo resultado en una mesa
    """
    data = request.get_json()
    json = miControladorResultado.create(data, id_mesa, id_candidato)
    return jsonify(json)


@app.route("/resultados/<string:id>", methods=["GET"])
def getResultado(id):
    """
    Obtener resultado especifico
    :param id: Identificación
    :return: Un resultado específico
    """
    json = miControladorResultado.show(id)
    return jsonify(json)


@app.route("/resultados/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=["PUT"])
def modificarResultado(id_resultado, id_mesa, id_candidato):
    """
    Modificar un resultado
    :param id_resultado: Identificación resultado
    :param id_mesa: Identificación mesa
    :param id_candidato: Identificación candidato
    :return: Resultado modificado
    """
    data={}
    json = miControladorResultado.update(id_resultado, data, id_mesa, id_candidato)
    return jsonify(json)


@app.route("/resultados/<string:id>", methods=["DELETE"])
def borrarResultado(id):
    """
    Eliminar Resultado
    :param id: Identificación
    :return: Resultado borrado
    """
    json = miControladorResultado.delete(id)
    return jsonify(json)


@app.route("/resultados/mesa/<string:id_mesa>", methods=["GET"])
def inscritosMesa(id_mesa):
    """
    Buscar los candidatos votados en una mesa por Id
    :param id_mesa: Identificación mesa
    :return: Candidatos inscritos en una mesa por Id
    """
    json = miControladorResultado.getListarCandidatosMesa(id_mesa)
    return jsonify(json)


@app.route("/resultados/mesas/<string:id_candidato>", methods=["GET"])
def inscritoEnMesas(id_candidato):
    """
    Buscar el candidato en las mesas
    :param id_candidato: Identificación candidato
    :return: Candidato inscrito en mesas
    """
    json = miControladorResultado.getListarMesasDeInscritoCandidato(id_candidato)
    return jsonify(json)


@app.route("/resultados/maxdocument", methods=["GET"])
def getMaxDocument():
    """
    Buscar total de votos
    :return: Total votos
    """
    json = miControladorResultado.getMayorCedula()
    return jsonify(json)


if __name__ == "__main__":
    app.run(debug=False, port=8081)