import psycopg2
from copy import deepcopy

class DataBase:
    # conexion = psycopg2.connect(host = "localhost", 
    #                         database = "aviacion",
    #                         user = "api_first_admin",
    #                         password = "equipo-rojo/proyecto-primer-parcial")

    conexion = psycopg2.connect(host = "localhost", 
                            database = "aviacion",
                            user = "postgres",
                            password = "peonmas123")


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

    def insert_persona(self, nss, nombre, telefono):
        cursor = self.conexion.cursor()
        cursor.execute(f"select per.sp_insert_persona('{nss}', '{nombre}', {telefono})")
        self.conexion.commit()
        cursor.close()

    def insert_corporacion(self, nombre, direccion, telefono):
        cursor = self.conexion.cursor()
        cursor.execute(f"select prop.sp_insert_corporacion('{nombre}', '{direccion}', {telefono})")
        self.conexion.commit()
        cursor.close()

    def insert_clase_hangar(self, capacidad):
        cursor = self.conexion.cursor()
        cursor.execute(f"select eq.sp_insert_clase_hangar({capacidad})")
        self.conexion.commit()
        cursor.close()

    def insert_tipo_avion(self, modelo, capacidad, peso_avion):
        cursor = self.conexion.cursor()
        cursor.execute(f"select eq.sp_insert_tipo_avion({modelo}, {capacidad}, {peso_avion})")
        self.conexion.commit()
        cursor.close()

    def update_persona(self, id, nss, nombre, telefono):
        cursor = self.conexion.cursor()
        cursor.execute(f"select per.sp_update_persona({id}, '{nss}', '{nombre}', {telefono})")
        self.conexion.commit()
        cursor.close()

    def update_corporacion(self, nombre, direccion, telefono):
        cursor = self.conexion.cursor()
        cursor.execute(f"select prop.sp_update_corporacion('{nombre}', '{direccion}', {telefono})")
        self.conexion.commit()
        cursor.close()

    def update_clase_hangar(self, num_hangar, capacidad):
        cursor = self.conexion.cursor()
        cursor.execute(f"select eq.sp_update_clase_hangar({num_hangar}, {capacidad})")
        self.conexion.commit()
        cursor.close()

    def update_tipo_avion(self, id, modelo, capacidad, peso_avion):
        cursor = self.conexion.cursor()
        cursor.execute(f"select eq.sp_update_tipo_avion({id}, '{modelo}', {capacidad}, {peso_avion})")
        self.conexion.commit()
        cursor.close()