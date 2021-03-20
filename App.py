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

if __name__ == '__main__':
    app.run(port=3000, debug=True)