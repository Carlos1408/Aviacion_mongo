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


#INSERTS
@app.route('/index_register_form/<table_name>', methods = ['GET'])
def index_register_form(table_name):
    return render_template('index_register_form.html',
                            table = db_data.get_table(table_name),
                            data_select = db_data.get_data_select(table_name))

@app.route('/insert_register/<schema>/<table_name>', methods = ['POST'])
def insert_register(schema, table_name):
    form_data = get_form_data(table_name, 'insert')
    print(form_data)
    if table_name == 'persona':
        try:
            return redirect(f"/index_register_form/persona_{request.form['tipo_persona']}")
        except:
            pass
    return redirect(f"/index-table/{schema}/{table_name}")
    

# UPDATES
@app.route('/index_update_form/<table_name>/<data>', methods = ['GET'])
def index_update_form(table_name, data):
    table = db_data.get_table_with_spec_row(table_name, data)
    return render_template('index_update_form.html',
                            table = table,
                            data_select = db_data.get_data_select(table_name),
                            default_values = table['spec_row'][0],
                            data = data)

@app.route('/update_register/<schema>/<table_name>/<data>', methods = ['POST'])
def update_register(schema, table_name, data):
    form_data = [data] + get_form_data(table_name, 'update')
    print(form_data)
    return redirect(f"/index-table/{schema}/{table_name}")

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

def get_form_data(table_name, operation):
    data = []
    table_info = db_data.get_info(table_name)
    for field in bd.select_fields_names(table_info['schema'], table_info['name']):
        if (operation == 'update' and field[0] != table_info['index']) or (operation == 'insert' and (field[0] != 'id' or table_name == 'empleados' or table_name == 'piloto')):
            data.append(request.form[field[0]])
    return data

if __name__ == '__main__':
    app.run(port=3000, debug=True)