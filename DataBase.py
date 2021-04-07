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

    def delete_row(self, table, condition):
        cursor = self.conexion.cursor()
        query = f"delete from {table} where {condition}"
        cursor.execute(query)
        self.conexion.commit()
        cursor.close()