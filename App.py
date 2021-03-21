from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

conexion = psycopg2.connect(host = "tuffi.db.elephantsql.com", database = "ewayqilc", user = "ewayqilc", password = "c_3fHeJM-wn6440Q4ZU0F9hf7dyDu9ba")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hangar/')
def hangares():
    cursor = conexion.cursor()
    query = "select * from clase_hangar"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('hangar.html', table = data)

@app.route('/persona')
def personas():
    cursor = conexion.cursor()
    query = "select * from persona"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('persona.html', table = data)

@app.route('/corporacion')
def corporacion():
    cursor = conexion.cursor()
    query = "select * from corporacion"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('corporacion.html', table = data)

@app.route("/add-hangar", methods = ['POST'])
def add_hangar():
    num_hangar = request.form['num_hangar']
    capacidad = request.form['capacidad']
    query = f"""insert into clase_hangar
                values({num_hangar}, {capacidad})"""
    cursor = conexion.cursor()
    cursor.execute(query)
    cursor.close()
    return redirect(url_for("hangares"))

@app.route("/add-persona", methods = ['POST'])
def add_persona():
    nss = request.form['nss']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    query = f"""insert into persona (nss, nombre, telefono)
                values({nss}, '{nombre}', {telefono})"""
    cursor = conexion.cursor()
    cursor.execute(query)
    cursor.close()
    return redirect(url_for("personas"))

@app.route("/add-corporacion", methods = ['POST'])
def add_corporacion():
    nombre = request.form['nombre_corporacion']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    query = f"""insert into corporacion(nombre, direccion, telefono)
                values('{nombre}', '{direccion}', {telefono})"""
    cursor = conexion.cursor()
    cursor.execute(query)
    cursor.close()

    return redirect(url_for("corporacion"))

if __name__ == '__main__':
    app.run(port=3000, debug=True)