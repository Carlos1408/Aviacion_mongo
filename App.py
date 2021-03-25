from flask import Flask, render_template, request, redirect, url_for, flash
from copy import deepcopy
import psycopg2

conexion = psycopg2.connect(host = "tuffi.db.elephantsql.com", database = "ewayqilc", user = "ewayqilc", password = "c_3fHeJM-wn6440Q4ZU0F9hf7dyDu9ba")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hangar/')
def hangares():
    data = select_all("clase_hangar")
    return render_template('body_data_table.html', table = data, direction = "hangar.html")

@app.route('/persona')
def personas():
    data = select_all("persona order by id")
    return render_template('body_data_table.html', table = data, direction = "persona.html")

@app.route('/corporacion')
def corporacion():
    data = select_all("corporacion")
    return render_template('body_data_table.html', table = data, direction = "corporacion.html")

@app.route('/tipo-avion')
def tipo_avion():
    data = select_all("tipo_avion order by id")
    return render_template('body_data_table.html', table = data, direction = "tipo_avion.html")

@app.route("/add-hangar", methods = ['POST'])
def add_hangar():
    num_hangar = request.form['num_hangar']
    capacidad = request.form['capacidad']
    query = f"""insert into clase_hangar
                values({num_hangar}, {capacidad})"""
    execute_query(query)
    return redirect(url_for("hangares"))

@app.route("/add-persona", methods = ['POST'])
def add_persona():
    nss = request.form['nss']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    query = f"""insert into persona (nss, nombre, telefono)
                values({nss}, '{nombre}', {telefono})"""
    execute_query(query)
    return redirect(url_for("personas"))

@app.route("/add-corporacion", methods = ['POST'])
def add_corporacion():
    nombre = request.form['nombre_corporacion']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    query = f"""insert into corporacion(nombre, direccion, telefono)
                values('{nombre}', '{direccion}', {telefono})"""
    execute_query(query)
    return redirect(url_for("corporacion"))

@app.route("/add-tipo-avion", methods = ['POST'])
def add_tipo_avion():
    modelo = request.form['modelo']
    capacidad = request.form['capacidad']
    peso = request.form['peso_avion']
    query = f"""insert into tipo_avion(modelo, capacidad, peso_avion)
                values('{modelo}'', {capacidad}, {peso})"""
    execute_query(query)
    return redirect(url_for('tipo_avion'))

# UPDATE CLASE_HANGAR
@app.route("/form-clase-hangar", methods = ['POST'])
def form_update_clase_hangar():
    num_hangar = request.form['num_hangar_update']
    data = select_row("clase_hangar", f"num_hangar = {num_hangar}")
    return render_template('body_data_table.html', table = data, direction = "updates/clase_hangar.html")

@app.route("/update-clase-hangar/<num_hangar>", methods = ['POST'])
def update_clase_hangar(num_hangar):
    capacidad = request.form['capacidad']
    query = f"update clase_hangar set capacidad = {capacidad} where num_hangar = {num_hangar}"
    execute_query(query)
    return redirect(url_for("hangares"))

# UPDATE CORPORACION
@app.route("/form-corporacion", methods = ['POST'])
def form_update_corporacion():
    nombre = request.form['nombre_update']
    data = select_row("corporacion", f"nombre = '{nombre}'")
    return render_template('body_data_table.html', table = data, direction = "updates/corporacion.html")

@app.route("/update-corporacion/<nombre>", methods = ['POST'])
def update_corporacion(nombre):
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    query = f"update corporacion set direccion = '{direccion}', telefono = {telefono} where nombre = '{nombre}'"
    execute_query(query)
    return redirect(url_for("corporacion"))

# UPDATE PERSONA
@app.route("/form-persona", methods = ['POST'])
def form_update_persona():
    id = request.form['id_update']
    data = select_row("persona", f"id = {id}")
    return render_template('body_data_table.html', table = data, direction = "updates/persona.html")

@app.route("/update-persona/<id>", methods = ['POST'])
def update_persona(id):
    nss = request.form['nss']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    query = f"update persona set nss = '{nss}', nombre = '{nombre}', telefono = {telefono} where id = {id}"
    execute_query(query)
    return redirect(url_for("personas"))

# UPDATE TIPO_AVION
@app.route("/form-tipo-avion", methods = ['POST'])
def form_update_tipo_avion():
    id = request.form['id_update']
    data = select_row("tipo_avion", f"id = {id}")
    return render_template('body_data_table.html', table = data, direction = "updates/tipo_avion.html")

@app.route("/update-tipo-avion/<id>", methods = ['POST'])
def update_tipo_avion(id):
    modelo = request.form['modelo']
    capacidad = request.form['capacidad']
    peso = request.form['peso']
    query = f"update tipo_avion set modelo = '{modelo}', capacidad = {capacidad}, peso_avion = {peso} where id = {id}"
    execute_query(query)
    return redirect(url_for("tipo_avion"))

def select_all(table):
    cursor = conexion.cursor()
    query = f"select * from {table}"
    cursor.execute(query)
    data = deepcopy(cursor.fetchall())
    cursor.close()
    return data

def select_row(table, condition):
    cursor = conexion.cursor()
    query = f"select * from {table} where {condition}"
    cursor.execute(query)
    data = deepcopy(cursor.fetchall())
    cursor.close()
    return data

def execute_query(query):
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    cursor.close()

def update_table(query):
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    cursor.close()

if __name__ == '__main__':
    app.run(port=3000, debug=True)