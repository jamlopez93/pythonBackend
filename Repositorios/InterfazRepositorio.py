from hashlib import new
from bson import DBRef
from bson.objectid import ObjectId
from typing import TypeVar, Generic, List,  get_origin, get_args
import database.database as dbase
import json

T = TypeVar('T')


class InterfazRepositorio(Generic[T]):

    def __init__(self):
        """
        constructor de la clase interfaz repositorio
        """
        self.db = dbase.dbConnection()
        theClass= get_args(self.__orig_bases__[0])
        self.collection = theClass[0].__name__.lower()

    def getValuesDBRefFromList(self, theList):
        """
        Obtiene los valores de ref de una lista
        :param theList: Lista de valores
        :return: Lista de valores de ref
        """
        newList = []
        laColeccion = self.db[theList[0]._id.collection]
        for item in theList:
            value = laColeccion.find_one({"_id": ObjectId(item.id)})
            value["_id"] = value["_id"].__str__()
            newList.append(value)
        return newList

    def getValuesDBRef(self, x):
        """
        Obtiene los valores de dbref
        :param x: valor de referencia
        :return: Lista valores de ref de db
        """
        keys = x.keys()
        for k in keys:
            if isinstance(x[k], DBRef):
                laColeccion = self.db[x[k].collection]
                valor = laColeccion.find_one({"_id": ObjectId(x[k].id)})
                valor["_id"] = valor["_id"].__str__()
                x[k] = valor
                x[k] = self.getValuesDBRef(x[k])
            elif isinstance(x[k], list) and len(x[k])>0:
                x[k]= self.getValuesDBRefFromList(x[k])
            elif isinstance(x[k], dict):
                x[k]= self.getValuesDBRef(x[k])
        return x

    def findById(self, id):
        """
        Función buscar por Id
        :param id: identificación
        :return: Un dato encontrado por Id
        """
        laColeccion = self.db[self.collection]
        x = laColeccion.find_one({"_id": ObjectId(id)})
        x = self.getValuesDBRef(x)
        if x == None:
            x = {}
        else:
            x["_id"] = x["_id"].__str__()
        return x

    def formatList(self, x):
        """
        Se da formato a una lista
        :param x: valor nueva lista
        :return: Nueva lista con formato
        """
        newList = []
        for item in x:
            if isinstance(item, ObjectId):
                newList.append(item.__str__())
        if len(newList) == 0:
            newList = x
        return newList

    def transformObjectIds(self, x):
        """
        Se transforma los objetos en sus IDs
        :param x: Atributo a transformar
        :return: Objetos transformados en IDs
        """
        for attribute in x.keys():
            if isinstance(x[attribute], ObjectId):
                x[attribute] = x[attribute].__str__()
            elif isinstance(x[attribute], list):
                x[attribute]= self.formatList(x[attribute])
            elif isinstance(x[attribute], dict):
                x[attribute]= self.transformObjectIds(x[attribute])
        return x

    def findAll(self):
        """
        Buscar todo en una collection
        :return: Todos los datos en una collection
        """
        laColeccion = self.db[self.collection]
        data = []
        for x in laColeccion.find():
            x["_id"] = x["_id"].__str__()
            x = self.transformObjectIds(x)
            x = self.getValuesDBRef(x)
            data.append(x)
        return data

    def update(self, id, item: T):
        """
        Update
        :param id: identificación (objeto) a buscar
        :param item: Tipo de dato a buscar (mesas, candidato, etc)
        :return: Cantidad de objetos actualizados
        """
        _id = ObjectId(id)
        laColeccion = self.db[self.collection]
        delattr(item, "_id")
        item = item.__dict__
        updateItem = {"$set": item}
        x = laColeccion.update_one({"_id":_id}, updateItem)
        return {"updated_count":x.matched_count}

    def delete(self, id):
        """
        delete collection
        :param id: Identificación
        :return: Collección borrada
        """
        laColeccion = self.db[self.collection]
        cuenta = laColeccion.delete_one({"_id": ObjectId(id)}).deleted_count
        return {"deleted_count": cuenta}

    def ObjectToDBRef(self, item: T):
        """
        Se obtienen objetos desde una dbref
        :param item: Tipo de objeto de referencia
        :return: Objetos desde una dbref
        """
        nameCollection = item.__class__.__name__.lower()
        return DBRef(nameCollection, ObjectId(item._id))


    def transformRefs(self, item):
        """
        Transforma las DBRefs
        :param item: Tipo de referencia a diccionario
        :return: DB refs transformadas
        """
        theDict = item.__dict__
        keys = list(theDict.keys())
        for k in keys:
            if theDict[k].__str__().count("object") ==1:
                newObject = self.ObjectToDBRef(getattr(item,k))
                setattr(item, k, newObject)
        return item


    def save(self, item: T):
        """
        Guardar collection
        :param item: tipo genérico
        :return: Collección guardada
        """
        laColeccion = self.db[self.collection]
        elId = ""
        item = self.transformRefs(item)
        if hasattr(item, "_id") and item._id != "":
            elId = item._id
            _id = ObjectId(elId)
            laColeccion  = self.db[self.collection]
            delattr(item, "_id")
            item = item.__dict__
            updateItem = {"$set":item}
            x = laColeccion.update_one({"_id": _id}, updateItem)
        else: 
            _id = laColeccion.insert_one(item.__dict__)
            elId = _id.inserted_id.__str__()
        x = laColeccion.find_one({"_id":ObjectId(elId)})
        x["_id"] = x["_id"].__str__()
        return self.findById(elId)


    def query(self, theQuery):
        """
        Querys especificos
        """

        laColeccion = self.db[self.collection]
        data = []
        for x in laColeccion.find(theQuery):
            x["_id"] = x["_id"].__str__()
            x = self.transformObjectIds(x)
            x = self.getValuesDBRef(x)
            data.append(x)
        return data

    def queryAggregation(self, theQuery):
        """
        Query agregación
        :param self: Agregar query
        :param theQuery: collección query
        :return: Query agregado
        """

        laColeccion = self.db[self.collection]
        data = []
        for x in laColeccion.aggregate(theQuery):
            x["_id"] = x["_id"].__str__()
            x = self.transformObjectIds(x)
            x = self.getValuesDBRef(x)
            data.append(x)
        return data

    