from Repositorios.MesaRepositorio import MesaRepositorio
from Modelos.Mesa import Mesa


class MesaControlador():

    def __init__(self):
        """
        Constructor de la clase mesa controlador
        """
        self.repositorioMesa = MesaRepositorio()

    def index(self):
        """
        Devuelve todos los documentos
        :return: Todos los documentos
        """
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        """
        Crea documentos
        :param infoMesa: Información mesa
        :return: Información de mesa nueva
        """
        nuevaMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        """
        Muestra un documento
        :param id: Identificación
        :return: Un docmento
        """
        laMesa = Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__

    def update(self, id, infoMesa):
        """
        Actualiza un documento
        :param id: Identificación
        :param infoMesa: Información de la mesa
        :return: Documento actualizado
        """
        MesaActual = Mesa(self.repositorioMesa.findById(id))
        MesaActual.numero = infoMesa["numero"]
        MesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(MesaActual)

    def delete(self, id):
        """
        Borra un documento
        :param id: Identificación
        :return: Documento borrado
        """
        return self.repositorioMesa.delete(id)
