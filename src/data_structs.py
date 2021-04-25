from DataBase import DataBase
db = DataBase

input_config = {'type':'',
                'name':'',
                'pleaceholder':''}

pk = {'clase_hangar': 'num_hangar',
        'avion': None,
        'tipo_avion': 'id',
        'servicio': 'tipo_servicio',
        'empleados': None,
        'persona': 'id',
        'corporacion': 'nombre',
        'piloto': 'num_lic'}

data_select = {'num_hangar' : db.select_fields(db, "num_hangar", "eq.clase_hangar order by num_hangar"),
                'piloto' : db.execute_query_returning_table(db, """select pi.num_lic, pe.nombre from eq.piloto pi inner join per.persona pe on pi.id = pe.id"""),
                'corporacion' : db.select_fields(db, "nombre", "prop.corporacion"),
                'tipo_avion' : db.select_fields(db, "id, modelo", "eq.tipo_avion order by tipo_avion"),
                'servicio' : db.select_fields(db, 'tipo_servicio', 'per.servicio')}


table_struct = {'clase_hangar' : {
                        'schema' : 'eq',
                        'table_name' : 'clase_hangar',
                        'fields' : db.select_fields_names(db, 'eq', 'clase_hangar'),
                        'data' : db.select_all(db, 'eq.clase_hangar')},
                'persona' : {
                        'schema' : 'per',
                        'table_name' : 'persona',
                        'fields' : db.select_fields_names(db, 'per', 'persona'),
                        'data' : db.select_all(db, 'per.persona')},
                'empleados' : {
                        'schema' : 'per',
                        'table_name' : 'empleados',
                        'fields' : db.select_fields_names(db, 'per', 'empleados'),
                        'data' : db.select_all(db, 'per.empleados')},
                'piloto' : {
                        'schema' : 'eq',
                        'table_name' : 'piloto',
                        'fields' : db.select_fields_names(db, 'eq', 'piloto'),
                        'data' : db.select_all(db, 'eq.piloto')},
                'corporacion' : {
                        'schema' : 'prop',
                        'table_name' : 'corporacion',
                        'fields' : db.select_fields_names(db, 'prop', 'corporacion'),
                        'data' : db.select_all(db, 'prop.corporacion')},
                'servicio' : {
                        'schema' : 'per',
                        'table_name' : 'servicio',
                        'fields' : db.select_fields_names(db, 'per', 'servicio'),
                        'data' : db.select_all(db, 'per.servicio')},
                'avion' : {
                        'schema' : 'eq',
                        'table_name' : 'avion',
                        'fields' : db.select_fields_names(db, 'eq', 'avion'),
                        'data' : db.select_all(db, 'eq.avion')},
                'tipo_avion' : {
                        'schema' : 'eq',
                        'table_name' : 'tipo_avion',
                        'fields' : db.select_fields_names(db, 'eq', 'tipo_avion'),
                        'data' : db.select_all(db, 'eq.tipo_avion')}}

