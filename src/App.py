from flask import Flask, render_template, request, redirect, url_for, flash
from DataBase import DataBase
from DB_data import DB_data

bd = DataBase()
db_data = DB_data()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index-table/<schema>/<table>')
def index_table(schema, table):
    return render_template('index_table.html', table = db_data.get_table(table))

@app.route('/index_register_form/<table_name>', methods = ['GET'])
def index_register_form(table_name):
    if table_name == 'avion' or table_name == 'empleados' or table_name == 'servicio':
        return render_template('index_register_form.html',
                                table = db_data.get_table(table_name),
                                data_select = db_data.get_data_select())
    else:
        return render_template('index_register_form.html',
                                table = db_data.get_table(table_name),
                                data_select = None)
    
@app.route('/index_update_form/<table_name>/<data>')
def index_update_form(table_name, data):
    table = db_data.get_table_with_spec_row(table_name, data)
    if table_name == 'avion' or table_name == 'empleados' or table_name == 'servicio':
        return render_template('index_update_form.html',
                                table = table,
                                data_select = db_data.get_data_select(),
                                data = data,
                                default_values = table['spec_row'][0])
    else:
        return render_template('index_update_form.html',
                                table = table,
                                data_select = None,
                                data = data,
                                default_values = table['spec_row'][0])

# INSERT CLASE_HANGAR
@app.route("/add-clase_hangar", methods = ['GET', 'POST'])
def add_hangar():
    if request.method == 'GET':
        return render_template('index_register_form.html',
                                table = ds.table_struct['clase_hangar'],
                                data_select = None)
    elif request.method == 'POST':
        num_hangar = request.form['num_hangar']
        capacidad = request.form['capacidad']
        print('POST', num_hangar, capacidad)
        return redirect('/index-table/eq/clase_hangar')

#INSERT PERSONA
@app.route("/add-persona", methods = ['GET', 'POST'])
def add_persona():
    if request.method == 'GET':
        return render_template('index_register_form.html',
                                table_name = 'persona',
                                schema = 'per',
                                data_select = None)
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
            return redirect('/index_register_form/empleados')
        elif tipo_persona == 'piloto':
            return redirect('index_register_form/piloto')
        return redirect('/index-table/per/persona')

#INSERT EMPLEADO
@app.route("/add-empleados", methods = ['GET', 'POST'])
def add_empleado():
    if request.method == 'GET':
        return render_template('index_register_form.html',
                                table_name = 'empleados',
                                schema = 'per',
                                data_select = ds.data_select)
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
        return render_template('index_register_form.html',
                                table_name = 'piloto',
                                schema = 'eq',
                                data_select = None)
    elif request.method == 'POST':
        num_lic = request.form['num_lic']
        print(num_lic)
        return redirect('/index-table/eq/piloto')

#INSERT CORPORACION
@app.route("/add-corporacion", methods = ['GET', 'POST'])
def add_corporacion():
    if request.method == 'GET':
        return render_template('index_register_form.html',
                                table_name = 'corporacion',
                                schema = 'prop',
                                data_select = None)
    elif request.method == 'POST':
        nombre = request.form['nombre_corporacion']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        print(nombre, direccion, telefono)
        return redirect('/index-table/prop/corporacion')

#INSERT AVION
@app.route("/add-avion", methods = ['GET', 'POST'])
def add_avion():
    if request.method == 'GET':
        return render_template('index_register_form.html',
                                table_name = 'avion',
                                schema = 'eq',
                                data_select = ds.data_select)
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
        return render_template('index_register_form.html',
                                table_name = 'tipo_avion',
                                schema = 'eq',
                                data_select = None)
    elif request.method == 'POST':
        modelo = request.form['modelo']
        capacidad = request.form['capacidad']
        peso = request.form['peso']
        return redirect('/index-table/eq/tipo_avion')

#INSERT SERVICIO
@app.route("/add-servicio", methods = ['GET', 'POST'])
def add_servicio():
    if request.method == 'GET':
        return render_template('index_register_form.html',
                                table_name = 'servicio',
                                schema = 'per',
                                data_select = ds.data_select)
    elif request.method == 'POST':
        tipo_servicio = request.form['tipo_servicio']
        horas = request.form['horas']
        tipo_avion = request.form['tipo_avion']
        print(tipo_servicio, horas, tipo_avion)
        return redirect('/index-table/per/servicio')

# UPDATE CLASE_HANGAR
@app.route("/update-clase_hangar/<num_hangar>", methods = ['GET', 'POST'])
def update_clase_hangar(num_hangar):
    if request.method == 'GET':
        data_fields = bd.select_fields_names('eq', 'clase_hangar')
        data = bd.select_row("eq.clase_hangar", f"num_hangar = {num_hangar}")
        return render_template('./updates/clase_hangar.html',
                                num_hangar = num_hangar,
                                fields = data_fields,
                                table = data,
                                table_name = 'Clase hangar')
    elif request.method == 'POST':
        print('UPDATE POST')
        num_hangar = request.form['num_hangar']
        capacidad = request.form['capacidad']
        print(num_hangar, capacidad)
        return redirect('/index-table/eq/clase_hangar')


# UPDATE CORPORACION
@app.route("/update-corporacion/<nombre>", methods = ['GET', 'POST'])
def update_corporacion(nombre):
    if request.method == 'GET':
        data_fields = bd.select_fields_names('prop', 'corporacion')
        data = bd.select_row("prop.corporacion", f"nombre = '{nombre}'")
        return render_template('./updates/corporacion.html',
                                nombre = nombre,
                                fields = data_fields,
                                table = data,
                                table_name = 'Corporacion')
    elif request.method == 'POST':
        print('UPDATE POST')
        return redirect('/index-table/prop/corporacion')


# UPDATE PERSONA
@app.route("/update-persona/<id>", methods = ['GET', 'POST'])
def update_persona(id):
    if request.method == 'GET':
        data_fields = bd.select_fields_names('per', 'persona')
        data = bd.select_row("per.persona", f"id = {id}")
        return render_template('./updates/persona.html',
                                id = id,
                                fields = data_fields,
                                table = data,
                                table_name = 'Corporacion')
    elif request.method == 'POST':
        print('UPDATE POST')
        return redirect('/index-table/per/persona')


# UPDATE TIPO_AVION
@app.route("/update-tipo_avion/<id>", methods = ['GET', 'POST'])
def update_tipo_avion(id):
    if request.method == 'GET':
        data_fields = bd.select_fields_names('eq', 'tipo_avion')
        data = bd.select_row("eq.tipo_avion", f"id = {id}")
        return render_template('./updates/tipo_avion.html',
                                id = id,
                                fields = data_fields,
                                table = data,
                                table_name = 'Tipo avion')
    elif request.method == 'POST':
        print('UPDATE POST')
        return redirect('/index-table/eq/tipo_avion')


# UPDATE AVION
@app.route("/update-avion/<matricula>", methods = ['GET', 'POST'])
def update_avion(matricula):
    if request.method == 'GET':
        data_num_hangar = bd.select_fields("num_hangar", "eq.clase_hangar order by num_hangar")
        data_piloto = bd.execute_query_returning_table("""select pi.num_lic, pe.nombre from eq.piloto pi
                                                        inner join per.persona pe on pi.id = pe.id""")
        data_corporacion = bd.select_fields("nombre", "prop.corporacion")
        data_tipo_avion = bd.select_fields("id, modelo", "eq.tipo_avion order by tipo_avion")
        data_fields = bd.select_fields_names('eq', 'avion')
        data = bd.select_row("eq.avion", f"matricula = '{matricula}'")
        return render_template('./updates/avion.html',
                                fields = data_fields,
                                table = data,
                                table_num_hangar = data_num_hangar,
                                table_piloto = data_piloto,
                                table_corporacion = data_corporacion,
                                table_tipo_avion = data_tipo_avion,
                                matricula = matricula,
                                table_name = 'Avion')
    elif request.method == 'POST':
        print('UPDATE POST')
        return redirect('/index-table/eq/avion')


# UPDATE EMPLEADO
@app.route("/update-empleados/<id>", methods = ['GET', 'POST'])
def update_empleado(id):
    if request.method == 'GET':
        data_fields = bd.select_fields_names('per', 'empleados')
        data = bd.select_row("per.empleados", f"id = '{id}'")
        data_tipo_servicio = bd.select_fields('tipo_servicio', 'per.servicio')
        return render_template('updates/empleado.html',
                                table_tipo_servicio = data_tipo_servicio,
                                id = id,
                                fields = data_fields,
                                table = data,
                                table_name = 'Empleados')
    elif request.method == 'POST':
        print('UPDATE POST')
        return redirect('/index-table/per/empleados')


# UPDATE PILOTO
@app.route("/update-piloto/<id>", methods = ['GET', 'POST'])
def update_piloto(id):
    if request.method == 'GET':
        data_fields = bd.select_fields_names('eq', 'piloto')
        data = bd.select_row("eq.piloto", f"id = {id}")
        return render_template('./updates/piloto.html',
                                id = id,
                                fields = data_fields,
                                table = data,
                                table_name = 'Piloto')
    elif request.method == 'POST':
        print('UPDATE POST')
        return redirect('/index-table/eq/piloto')


# UPDATE SERVICIO
@app.route("/update-servicio/<tipo_servicio>", methods = ['GET', 'POST'])
def update_servicio(tipo_servicio):
    if request.method == 'GET':
        data_fields = bd.select_fields_names('per', 'servicio')
        data = bd.select_row("per.servicio", f"tipo_servicio = '{tipo_servicio}'")
        data_tipo_avion = bd.select_fields("id, modelo", "eq.tipo_avion order by tipo_avion")
        return render_template('./updates/servicio.html',
                                table_tipo_avion = data_tipo_avion,
                                tipo_servicio = tipo_servicio,
                                fields = data_fields,
                                table = data,
                                table_name = 'Servicio')
    elif request.method == 'POST':
        print('UPDATE POST')
        return redirect('/index-table/per/servicio')

# UPDATE REDIRECCION A FORMULARIOS
@app.route("/request-update/<table>", methods = ['POST'])
def update(table):
    data = request.form['data']
    return redirect(f"/index_update_form/{table}/{data}")

# DELETE
@app.route("/delete/<schema>/<table>/<field>/<reg>")
def delete(schema, table, field, reg):
    query = f"delete from {schema}.{table} where {field} = '{reg}'"
    print(query)
    return redirect(f"/index-table/{schema}/{table}")

if __name__ == '__main__':
    app.run(port=3000, debug=True)