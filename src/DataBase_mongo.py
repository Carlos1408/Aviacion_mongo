import pymongo
from pymongo import MongoClient
from copy import deepcopy

class DataBase_mongo:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.aviacion

    def find(self, collection):
        idx = self.get_index(collection)
        collection = self.db[collection]
        return deepcopy(collection.find().sort(idx))

    def find_one(self, collection, field, value):
        collection = self.db[collection]
        data = collection.find_one({field:value})
        return deepcopy(data)

    def find_many(self, collection, field, value):
        idx = self.get_index(collection)
        collection = self.db[collection]
        data = collection.find({field:value}).sort(idx)
        return deepcopy(data)

    def get_fields(self, collection):
        collection = self.db[collection]
        data = collection.find_one()
        tags = list(data.keys())
        tags.remove('_id')
        return deepcopy(tags)

    def get_index(self, collection):
        data = self.get_fields(collection)
        return deepcopy(data[0])

    def get_info(self, collection):
        if collection == 'persona_empleados':
            collection = 'empleados'
        elif collection == 'persona_piloto':
            collection = 'piloto'
        return {
            'name':collection,
            'index':self.get_index(collection),
            'fields':self.get_fields(collection)
        }

    def get_index_list(self, collection):
        idx = self.get_index(collection)
        return [i[idx] for i in self.find(collection)]

    def get_max_index(self, collection):
        return max(self.get_index_list(collection))

    def get_field_data(self, collection, fields):
        if collection == 'persona':
            pilotos = self.get_index_list('piloto')
            empleados = self.get_index_list('empleados')
            asignados = list(set(pilotos) | set(empleados))
            table = self.db['persona'].find({ 'id' : { '$nin' : asignados}}).sort('id')
        else:
            table = self.find(collection)
        data = []
        for doc in table:
            row = []
            for field in fields:
                row.append(doc[field])
            data.append(row)
        return data

    def get_data_select(self, collection):
        if collection == 'avion':
            data_select = {
                'num_hangar':self.get_field_data('clase_hangar', ('num_hangar',)),
                'piloto':self.get_field_data('piloto', ('id', 'num_lic')),
                'corporacion':self.get_field_data('corporacion', ('nombre',)),
                'tipo_avion':self.get_field_data('tipo_avion', ('id', 'modelo'))
            }
        elif collection == 'empleados':
            data_select = {
                'servicio': self.get_field_data('servicio', ('tipo_servicio',)),
                'id': self.get_field_data('persona', ('id', 'nombre')),
                'generated_id':''
            }
        elif collection == 'persona_empleados':
            data_select = {
                'servicio': self.get_field_data('servicio', ('tipo_servicio',)),
                'id': self.get_field_data('persona', ('id', 'nombre')),
                'generated_id': self.get_max_index('persona')
            }
        elif collection == 'piloto':
            data_select = {
                'id': self.get_field_data('persona', ('id', 'nombre')),
                'generated_id': ''
            }
        elif collection == 'persona_piloto':
            data_select = {
                'id': self.get_field_data('persona', ('id', 'nombre')),
                'generated_id': self.get_max_index('persona')
            }
        elif collection == 'servicio':
            data_select = {
                'tipo_avion': self.get_field_data('tipo_avion', ('id', 'modelo'))
            }
        else:
            data_select = None
        return data_select

    def insert(self, collection, values):
        fields = self.get_fields(collection)
        if collection in ['persona', 'tipo_avion']:
            id = self.get_max_index(collection) + 1
            values = tuple([id] + list(values))
        document = dict(zip(fields, values))
        col = self.db[collection]
        col.insert_one(document)
    
    def remove(self, collection, index, value): 
        try:
            value =int(value)
        except:
            pass
        col = self.db[collection]
        col.delete_one({index : value})

    def update(self, collection, index, values):
         col = self.db[collection]
         fields = self.get_fields(collection)
         index_field = fields.pop(0)
         query = {index_field : index}
         values_dict = dict(zip(fields, values))
         new_values = {'$set' : values_dict}
         col.update_one(query, new_values)

    def enlist_collection(self, data):
        result = list()
        for row in data:
            aux = tuple(row.values())
            result.append(aux[1:])
        return result