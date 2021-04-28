from DataBase import DataBase

class DB_data:
    def __init__(self):
        self.db = DataBase()
        self.tables = {'clase_hangar' : {
                        'schema' : 'eq',
                        'name' : 'clase_hangar',
                        'index' : 'num_hangar'},
                'persona' : {
                        'schema' : 'per',
                        'name' : 'persona',
                        'index' : 'id'},
                'empleados' : {
                        'schema' : 'per',
                        'name' : 'empleados',
                        'index' : 'id'},
                'piloto' : {
                        'schema' : 'eq',
                        'name' : 'piloto',
                        'index' : 'id'},
                'corporacion' : {
                        'schema' : 'prop',
                        'name' : 'corporacion',
                        'index' : 'nombre'},
                'servicio' : {
                        'schema' : 'per',
                        'name' : 'servicio',
                        'index' : 'tipo_servicio'},
                'avion' : {
                        'schema' : 'eq',
                        'name' : 'avion',
                        'index' : 'matricula'},
                'tipo_avion' : {
                        'schema' : 'eq',
                        'name' : 'tipo_avion',
                        'index' : 'id'}}
        
    def get_table(self, table_name):
        table = self.tables[table_name]
        table['fields'] = self.db.select_fields_names(table['schema'], table['name'])
        table['data'] = self.db.select_all(f"{table['schema']}.{table['name']} order by {table['index']}")
        return table

    def get_table_with_spec_row(self, table_name, index):
        table = self.get_table(table_name)
        table['spec_row'] = self.db.select_row(f"{table['schema']}.{table['name']}", f"{table['index']} = '{index}'")
        return table

    def get_data_select(self, table_name):
        if table_name == 'avion' or table_name == 'empleados' or table_name == 'servicio':
                data_select = {'num_hangar' : self.db.select_fields("num_hangar", "eq.clase_hangar order by num_hangar"),
                                'piloto' :self. db.execute_query_returning_table("select pi.num_lic, pe.nombre from eq.piloto pi inner join per.persona pe on pi.id = pe.id"),
                                'corporacion' : self.db.select_fields("nombre", "prop.corporacion"),
                                'tipo_avion' : self.db.select_fields("id, modelo", "eq.tipo_avion order by tipo_avion"),
                                'servicio' : self.db.select_fields('tipo_servicio', 'per.servicio')}
        else:
                data_select = None
        return data_select

    def get_info(self, table_name):
                return self.tables[table_name]