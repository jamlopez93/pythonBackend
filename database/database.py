from pymongo import MongoClient
import json
import certifi

ca = certifi.where()


def loadConfigFile():
    """
    Cargar base de datos
    :return: Base de datos
    """
    with open('database/config.json') as f:
        data = json.load(f)
    return data


def dbConnection():
    """
    Conexión local y a mongo
    :return: Conexión Base de datos
    """
    dataConfig = loadConfigFile()
    try:
        client = MongoClient(dataConfig['db_connection'], tlsCAFile=ca)
        db = client["academic_db"]
    except ConnectionError:
        print("Error de conexión con la db")
    return db














