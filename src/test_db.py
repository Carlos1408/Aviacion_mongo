from DataBase_mongo import DataBase_mongo
from pprint import pprint

db = DataBase_mongo()
# documents = db.get_all('persona')
# documents = db.get_spec_document('persona', 'id', 1)
# documents = db.get_tags_names('persona')
# documents = db.get_collection_index('tipo_avion')

# if isinstance(documents, (list, tuple)):
#     for document in documents:
#         pprint.pprint(document)
# else:
#     pprint.pprint(documents)

# result = db.get_field_data('persona', ('id', 'nombre', 'telefono'))
result = db.find('persona')
print(type(result))
result = tuple(result)
print(type(result))
for res in result:
    pprint(res)
print('')

result = db.enlist_collection(result)
for res in result:
    print(res)