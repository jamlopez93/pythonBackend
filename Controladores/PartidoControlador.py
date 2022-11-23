from Repositorios.PartidoRepositorio import PartidoRepositorio
from Modelos.Partido import Partido


class PartidoControlador():

    def __init__(self):
        """
        Constructor de la clase partido controlador
        """
        self.repositorioPartido = PartidoRepositorio()

    def index(self):
        """
        Devuelve todos los documentos
        :return: Retorna todos los documentos de una colección
        """
        return self.repositorioPartido.findAll()


    def create(self, infoPartido):
        """
        Crea documentos
        :param infoPartido: Datos del partido
        :return: repositorio nuevo partido
        """
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)


    def show(self, id):
        """
        Mostrar un documento
        :param id: identificación partido
        :return: El partido como diccionario
        """
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__


    def update(self, id, infoPartido):
        """
        Actualiza un documento
        :param id: identificación partido
        :param infoPartido: información del partido
        :return: Información del nuevo partido actualizada
        """
        PartidoActual = Partido(self.repositorioPartido.findById(id))
        PartidoActual.nombre = infoPartido["nombre"]
        PartidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(PartidoActual)


    def delete(self, id):
        """
        Borra un documento
        :param id: identificación partido
        :return: Repositorio partido eliminado
        """
        return self.repositorioPartido.delete(id)
