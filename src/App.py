from flask import Flask, render_template, request, redirect, url_for, flash
from DataBase import DataBase

bd = DataBase()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index-table/<schema>/<table>')
def index_table(schema, table):
    data_fields = bd.execute_query_returning_table(f"SELECT column_name FROM information_schema.columns WHERE table_schema = '{schema}' AND table_name = '{table}'")
    data = bd.select_all(f"{schema}.{table}")
    return render_template('index_table.html', table = data, fields = data_fields, table_name = table)
    # return redirect(url_for('index'))

# INSERT CLASE_HANGAR
@app.route("/add-clase_hangar", methods = ['GET', 'POST'])
def add_hangar():
    if request.method == 'GET':
        print('GET')
        return render_template('register_forms/hangar.html')
    elif request.method == 'POST':
        num_hangar = request.form['num_hangar']
        capacidad = request.form['capacidad']
        print('POST', num_hangar, capacidad)
        return redirect('/index-table/eq/clase_hangar')

#INSERT PERSONA
@app.route("/add-persona", methods = ['GET', 'POST'])
def add_persona():
    if request.method == 'GET':
        return render_template('register_forms/persona.html')
    elif request.method == 'POST':
        nss = request.form['nss']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        try:
            tipo_persona = request.form['tipo_persona']
        except:
            tipo_persona = 'persona'
        print(nss, nombre, telefono, tipo_persona)
        if tipo_persona == 'empleado':
            return redirect(url_for("add_empleado"))
        elif tipo_persona == 'piloto':
            return redirect(url_for("add_piloto"))
        return redirect('/index-table/per/persona')

#INSERT EMPLEADO
@app.route("/add-empleados", methods = ['GET', 'POST'])
def add_empleado():
    if request.method == 'GET':
        data_tipo_servicio = bd.select_fields('tipo_servicio', 'per.servicio')
        return render_template('register_forms/empleado.html', table_tipo_servicio = data_tipo_servicio)
    elif request.method == 'POST':
        salario = request.form['salario']
        turno = request.form['turno']
        tipo_servicio = request.form['tipo_servicio']
        print(salario, turno, tipo_servicio)
        return redirect('/index-table/per/empleados')

#INSERT PILOTO
@app.route("/add-piloto", methods = ['GET', 'POST'])
def add_piloto():
    if request.method == 'GET':
        return render_template('register_forms/piloto.html')
    elif request.method == 'POST':
        num_lic = request.form['num_lic']
        print(num_lic)
        return redirect('/index-table/eq/piloto')

#INSERT CORPORACION
@app.route("/add-corporacion", methods = ['GET', 'POST'])
def add_corporacion():
    if request.method == 'GET':
        return render_template('register_forms/corporacion.html')
    elif request.method == 'POST':
        nombre = request.form['nombre_corporacion']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        return redirect('/index-table/prop/corporacion')

#INSERT AVION
@app.route("/add-avion", methods = ['GET', 'POST'])
def add_avion():
    if request.method == 'GET':
        data_num_hangar = bd.select_fields("num_hangar", "eq.clase_hangar order by num_hangar")
        data_piloto = bd.execute_query_returning_table("""select pi.num_lic, pe.nombre from eq.piloto pi
                                                        inner join per.persona pe on pi.id = pe.id""")
        data_corporacion = bd.select_fields("nombre", "prop.corporacion")
        data_tipo_avion = bd.select_fields("id, modelo", "eq.tipo_avion order by tipo_avion")
        return render_template('register_forms/avion.html',
                                table_num_hangar = data_num_hangar,
                                table_piloto = data_piloto,
                                table_corporacion = data_corporacion,
                                table_tipo_avion = data_tipo_avion)
    elif request.method == 'POST':
        matricula = request.form['matricula']
        num_hangar = request.form['num_hangar']
        piloto = request.form['piloto']
        corporacion = request.form['corporacion']
        tipo_avion = request.form['tipo_avion']
        print(matricula, num_hangar, piloto, corporacion, tipo_avion)
        return redirect('/index-table/eq/avion')

#INSERT TIPO_AVION
@app.route("/add-tipo_avion", methods = ['GET', 'POST'])
def add_tipo_avion():
    if request.method == 'GET':
        return render_template('register_forms/tipo_avion.html')
    elif request.method == 'POST':
        modelo = request.form['modelo']
        capacidad = request.form['capacidad']
        peso = request.form['peso']
        return redirect('/index-table/eq/tipo_avion')

#INSERT SERVICIO
@app.route("/add-servicio", methods = ['GET', 'POST'])
def add_servicio():
    if request.method == 'GET':
        data_tipo_avion = bd.select_fields("id, modelo", "eq.tipo_avion order by tipo_avion")
        return render_template('register_forms/servicio.html', table_tipo_avion = data_tipo_avion)
    elif request.method == 'POST':
        tipo_servicio = request.form['tipo_servicio']
        horas = request.form['horas']
        tipo_avion = request.form['tipo_avion']
        print(tipo_servicio, horas, tipo_avion)
        return redirect('/index-table/per/servicio')

# UPDATE CLASE_HANGAR
@app.route("/form-clase-hangar", methods = ['POST'])
def form_update_clase_hangar():
    num_hangar = request.form['num_hangar_update']
    data_fields = ('Numero de hangar', 'Capacidad')
    data = bd.select_row("eq.clase_hangar", f"num_hangar = {num_hangar}")
    try:
        return render_template('updates/clase_hangar.html', table = data, fields = data_fields)
    except:
        return redirect(url_for("hangares"))

@app.route("/update-clase-hangar/<num_hangar>", methods = ['POST'])
def update_clase_hangar(num_hangar):
    capacidad = request.form['capacidad']
    # query = f"update eq.clase_hangar set capacidad = {capacidad} where num_hangar = {num_hangar}"
    # bd.execute_query(query)
    bd.update_clase_hangar(num_hangar, capacidad)
    print(num_hangar, capacidad)
    return redirect(url_for("hangares"))

# UPDATE CORPORACION
@app.route("/form-corporacion", methods = ['POST'])
def form_update_corporacion():
    nombre = request.form['nombre_update']
    data_fields = ('Nombre', 'Direccion', 'Telefono')
    data = bd.select_row("prop.corporacion", f"nombre = '{nombre}'")
    try:
        return render_template('updates/corporacion.html', table = data, fields = data_fields)
    except:
        return redirect(url_for('corporacion'))

@app.route("/update-corporacion/<nombre>", methods = ['POST'])
def update_corporacion(nombre):
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    print(nombre, direccion, telefono)
    # query = f"update prop.corporacion set direccion = '{direccion}', telefono = {telefono} where nombre = '{nombre}'"
    # bd.execute_query(query)
    bd.update_corporacion(nombre, direccion, telefono)
    return redirect(url_for("corporacion"))

# UPDATE PERSONA
@app.route("/form-persona", methods = ['POST'])
def form_update_persona():
    id = request.form['id_update']
    data_fields = ('Id', 'NSS', 'Nombre', 'Telefono')
    data = bd.select_row("per.persona", f"id = {id}")
    try:
        return render_template('updates/persona.html', table = data, fields = data_fields)
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
    data_fields = ('Id', 'Modelo', 'Capacidad', 'Peso del avion')
    data = bd.select_row("eq.tipo_avion", f"id = {id}")
    try:
        return render_template('updates/tipo_avion.html', table = data, fields = data_fields)
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