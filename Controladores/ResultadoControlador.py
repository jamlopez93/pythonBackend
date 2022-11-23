from Repositorios.ResultadoRepositorio import ResultadoRepositorio
from Repositorios.MesaRepositorio import MesaRepositorio
from Repositorios.CandidatoRepositorio import CandidatoRepositorio

from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa


class ResultadoControlador():
    def __init__(self):
        """
        Constructor de la clase resultado controlador
        """
        self.repositorioResultado = ResultadoRepositorio()
        self.repositorioCandidato = CandidatoRepositorio()
        self.repositorioMesa = MesaRepositorio()

    def index(self):
        """
        Get all resultados
        :return: Agrega todos los resultados
        """
        return self.repositorioResultado.findAll()

    def create(self, infoResultado, id_mesa, id_candidato):
        """
        Insert resultado
        :param infoResultado: Información resultado
        :param id_mesa: Identificación mesa
        :param id_candidato: Identificación candidato
        :return: Resultado creado
        """
        nuevoResultado = Resultado(infoResultado)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        """
        Get one resultado by ID
        :param id: Identificación
        :return: diccionario resultado
        """
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    def update(self, id, infoResultado, id_mesa, id_candidato):
        """
        Update resultado
        :param id: identificación
        :param infoResultado: Información resultado
        :param id_mesa: Identificación mesa
        :param id_candidato: Identificación candidato
        :return: Resultado actualizado
        """
        elResultado = Resultado(self.repositorioResultado.findById(id))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)

    def delete(self, id):
        """
        Delete resultado
        :param id: identificación
        :return: Resultado eliminado
        """
        return self.repositorioResultado.delete(id)

    def getListarCandidatosMesa(self, id_mesa):
        """
        Get candidatos mesa
        :param id_mesa: Identificación candidato
        :return: Lista de candidatos por mesa
        """
        return self.repositorioResultado.getListadoCandidatosInscritosMesa(id_mesa)

    def getListarMesasDeInscritoCandidato(self, id_candidato):
        """
        Get candidatos inscritos
        :param id_candidato: Identificación candidato
        :return: Lista candidados inscritos
        """
        return self.repositorioResultado.getListadoMesasCandidatoInscrito(id_candidato)

    def getMayorCedula(self):
        """
        Get resultado mayor cédula
        :return: Resultado mayor candidato por cédula
        """
        return self.repositorioResultado.getNumeroCedulaMayorCandidato()