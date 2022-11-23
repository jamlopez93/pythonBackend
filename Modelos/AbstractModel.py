from abc import ABCMeta


class AbstractModel(metaclass=ABCMeta):
    def __init__(self, data):
        """
        Constructor de la clase AbstractModel
        :param data: datos a recibir de la sotras clases
        """
        for llave, valor in data.items():
            setattr(self, llave, valor)