import psycopg2
from copy import deepcopy

class DataBase:
    conexion = psycopg2.connect(host = "localhost",
                            database = "aviacion",
                            user = "api_first_admin",
                            password = "equipo-rojo/proyecto-primer-parcial")

    def __init__(self):
        pass

    def select_all(self, table):
        cursor = self.conexion.cursor()
        query = f"select * from {table}"
        cursor.execute(query)
        data = deepcopy(cursor.fetchall())
        cursor.close()
        return data

    def select_row(self, table, condition):
        cursor = self.conexion.cursor()
        query = f"select * from {table} where {condition}"
        cursor.execute(query)
        data = deepcopy(cursor.fetchall())
        cursor.close()
        return data

    def execute_query(self, query):
        cursor = self.conexion.cursor()
        cursor.execute(query)
        self.conexion.commit()
        cursor.close()

    def execute_query_returning_table(self, query):
        cursor = self.conexion.cursor()
        cursor.execute(query)
        data = deepcopy(cursor.fetchall())
        self.conexion.commit()
        cursor.close()
        return data

    def select_fields(self, fields, table):
        cursor = self.conexion.cursor()
        query = f"select {fields} from {table}"
        cursor.execute(query)
        data = deepcopy(cursor.fetchall())
        self.conexion.commit()
        cursor.close()
        return data

    def select_fields_names(self, schema, table):
        cursor = self.conexion.cursor()
        cursor.execute(f"""SELECT column_name
                            FROM information_schema.columns
                            WHERE table_schema = '{schema}'
                            AND table_name = '{table}'""")
        data = deepcopy(cursor.fetchall())
        self.conexion.commit()
        cursor.close()
        return data

    def insert_reg(self, table_info, values):
        print(f"select {table_info['schema']}.sp_insert_{table_info['name']}{values}")
        cursor = self.conexion.cursor()
        cursor.callproc(f"{table_info['schema']}.sp_insert_{table_info['name']}", values)
        self.conexion.commit()
        cursor.close()

    def update_reg(self, table_info, values):
        print(f"select {table_info['schema']}.sp_update_{table_info['name']}{values}")
        cursor = self.conexion.cursor()
        cursor.callproc(f"{table_info['schema']}.sp_update_{table_info['name']}", values)
        self.conexion.commit()
        cursor.close()

    def delete_reg(self, table_info, value):
        print(f"select {table_info['schema']}.sp_delete_{table_info['name']}{value}")
        cursor = self.conexion.cursor()
        cursor.callproc(f"{table_info['schema']}.sp_delete_{table_info['name']}", value)
        self.conexion.commit()
        cursor.close()

    def get_message(self):
        return self.conexion.notices[-1].replace('NOTICE:  ', '')