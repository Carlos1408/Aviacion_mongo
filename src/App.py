from flask import Flask, render_template, request, redirect, url_for, flash
from DataBase import DataBase

bd = DataBase()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hangar/')
def hangares():
    data = bd.select_all("eq.clase_hangar order by num_hangar")
    return render_template('body_data_table.html', table = data, direction = "hangar.html")

@app.route('/persona')
def personas():
    data = bd.select_all("per.persona order by id")
    return render_template('body_data_table.html', table = data, direction = "persona.html")

@app.route('/corporacion')
def corporacion():
    data = bd.select_all("prop.corporacion")
    return render_template('body_data_table.html', table = data, direction = "corporacion.html")

@app.route('/tipo-avion')
def tipo_avion():
    data = bd.select_all("eq.tipo_avion order by id")
    return render_template('body_data_table.html', table = data, direction = "tipo_avion.html")

# INSERT CLASE_HANGAR
@app.route("/add-hangar", methods = ['POST'])
def add_hangar():
    
    num_hangar = request.form['num_hangar']
    capacidad = request.form['capacidad']
    reg = bd.select_row("eq.clase_hangar", f"num_hangar = {num_hangar}")
    if len(reg) == 0:
        # query = f"""insert into eq.clase_hangar
        #             values({num_hangar}, {capacidad})"""
        # bd.execute_query(query)
        bd.insert_clase_hangar(capacidad)
    return redirect(url_for("hangares"))

#INSERT PERSONA
@app.route("/add-persona", methods = ['POST'])
def add_persona():
    nss = request.form['nss']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    # query = f"""insert into per.persona (nss, nombre, telefono)
    #             values({nss}, '{nombre}', {telefono})"""
    # bd.execute_query(query)
    bd.insert_persona(nss, nombre, telefono)
    return redirect(url_for("personas"))

#INSERT CORPORACION
@app.route("/add-corporacion", methods = ['POST'])
def add_corporacion():
    nombre = request.form['nombre_corporacion']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    reg = bd.select_row("prop.corporacion", f"nombre = '{nombre}'")
    if len(reg) == 0:
        # query = f"""insert into prop.corporacion(nombre, direccion, telefono)
        #             values('{nombre}', '{direccion}', {telefono})"""
        # bd.execute_query(query)
        bd.insert_corporacion(nombre, direccion, telefono)
    return redirect(url_for("corporacion"))

#INSERT TIPO_AVION
@app.route("/add-tipo-avion", methods = ['POST'])
def add_tipo_avion():
    modelo = request.form['modelo']
    capacidad = request.form['capacidad']
    peso = request.form['peso']
    # query = f"""insert into eq.tipo_avion(modelo, capacidad, peso_avion)
    #             values('{modelo}', {capacidad}, {peso})"""
    # bd.execute_query(query)
    bd.insert_tipo_avion(modelo, capacidad, peso)
    return redirect(url_for('tipo_avion'))

# UPDATE CLASE_HANGAR
@app.route("/form-clase-hangar", methods = ['POST'])
def form_update_clase_hangar():
    num_hangar = request.form['num_hangar_update']
    data = bd.select_row("eq.clase_hangar", f"num_hangar = {num_hangar}")
    try:
        return render_template('body_data_table.html', table = data, direction = "updates/clase_hangar.html")
    except:
        return redirect(url_for("hangares"))

@app.route("/update-clase-hangar/<num_hangar>", methods = ['POST'])
def update_clase_hangar(num_hangar):
    capacidad = request.form['capacidad']
    # query = f"update eq.clase_hangar set capacidad = {capacidad} where num_hangar = {num_hangar}"
    # bd.execute_query(query)
    bd.update_clase_hangar(num_hangar, capacidad)
    return redirect(url_for("hangares"))

# UPDATE CORPORACION
@app.route("/form-corporacion", methods = ['POST'])
def form_update_corporacion():
    nombre = request.form['nombre_update']
    data = bd.select_row("prop.corporacion", f"nombre = '{nombre}'")
    try:
        return render_template('body_data_table.html', table = data, direction = "updates/corporacion.html")
    except:
        return redirect(url_for('corporacion'))

@app.route("/update-corporacion/<nombre>", methods = ['POST'])
def update_corporacion(nombre):
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    # query = f"update prop.corporacion set direccion = '{direccion}', telefono = {telefono} where nombre = '{nombre}'"
    # bd.execute_query(query)
    bd.update_corporacion(nombre, direccion, telefono)
    return redirect(url_for("corporacion"))

# UPDATE PERSONA
@app.route("/form-persona", methods = ['POST'])
def form_update_persona():
    id = request.form['id_update']
    data = bd.select_row("per.persona", f"id = {id}")
    try:
        return render_template('body_data_table.html', table = data, direction = "updates/persona.html")
    except:
        redirect(url_for('personas'))

@app.route("/update-persona/<id>", methods = ['POST'])
def update_persona(id):
    nss = request.form['nss']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    # query = f"update per.persona set nss = '{nss}', nombre = '{nombre}', telefono = {telefono} where id = {id}"
    # bd.execute_query(query)
    bd.update_persona(id, nss, nombre, telefono)
    return redirect(url_for("personas"))

# UPDATE TIPO_AVION
@app.route("/form-tipo-avion", methods = ['POST'])
def form_update_tipo_avion():
    id = request.form['id_update']
    data = bd.select_row("eq.tipo_avion", f"id = {id}")
    try:
        return render_template('body_data_table.html', table = data, direction = "updates/tipo_avion.html")
    except:
        return redirect(url_for('tipo_avion'))

@app.route("/update-tipo-avion/<id>", methods = ['POST'])
def update_tipo_avion(id):
    modelo = request.form['modelo']
    capacidad = request.form['capacidad']
    peso = request.form['peso']
    # query = f"update eq.tipo_avion set modelo = '{modelo}', capacidad = {capacidad}, peso_avion = {peso} where id = {id}"
    # bd.execute_query(query)
    bd.update_tipo_avion(id, modelo, capacidad, peso)
    return redirect(url_for("tipo_avion"))

# DELETE ROW
@app.route('/delete_row/<table>/<field>/<data>/<url>')
def delete_row(table, field, data, url):
    print(table, field, data, url)
    print(table, f"{field} = '{data}'")
    bd.delete_row(table, f"{field} = '{data}'")
    return redirect(url_for(url))

if __name__ == '__main__':
    app.run(port=3000, debug=True)