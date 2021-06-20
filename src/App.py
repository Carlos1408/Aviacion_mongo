from flask import Flask, render_template, request, redirect, url_for, flash
from DataBase import DataBase
from DB_data import DB_data
from DataBase_mongo import DataBase_mongo

bd = DataBase()
db_data = DB_data()

mongo = DataBase_mongo()

app = Flask(__name__)
app.secret_key = "mysecretkey"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index-table/<collection>', methods=['GET', 'POST'])
def index_table(collection):
    data_table = mongo.get_info(collection)
    if request.method == 'GET':

        data_table['data'] = mongo.find(collection)

    elif request.method == 'POST':
        data = request.form['data']
        field = request.form['field']
        try:
            data = int(data)
        except:
            pass
        try:
            data_table['data'] = mongo.find_many(collection, field, data)
            # Editar data del documento
            if not data_table['data']:
                flash(
                    f"ERROR: {collection.capitalize().replace('_', ' ')} ({field.capitalize()}: {data}) Registro inexistente")
                return redirect(f"/index-table/{data_table['name']}")
        except:
            flash(f"ERROR: Error producido en la busqueda")
            return redirect(f"/index-table/{data_table['name']}")
    return render_template('index_table.html', table=data_table)


# INSERTS
@app.route('/index_register_form/<collection>', methods=['GET'])
def index_register_form(collection):
    return render_template('index_register_form.html',
                           table=mongo.get_info(collection),
                           data_select=mongo.get_data_select(collection))


@app.route('/insert_register/<collection>', methods=['POST'])
def insert_register(collection):
    form_data = get_form_data(collection, 'insert')
    print(form_data)
    # bd.insert_reg(db_data.get_info(collection), form_data)
    flash('Exito')
    mongo.insert(collection, form_data)
    # flash(bd.get_message())
    if collection == 'persona':
        try:
            return redirect(f"/index_register_form/persona_{request.form['tipo_persona']}")
        except:
            pass
    return redirect(f"/index-table/{collection}")


# UPDATES
@app.route('/index_update_form/<table_name>/<data>', methods=['GET'])
def index_update_form(table_name, data):
    table = db_data.get_table_with_spec_row(table_name, data)
    return render_template('index_update_form.html',
                           table=table,
                           data_select=db_data.get_data_select(table_name),
                           default_values=table['spec_row'][0],
                           data=data)


@app.route('/update_register/<schema>/<table_name>/<data>', methods=['POST'])
def update_register(schema, table_name, data):
    form_data = tuple([data]) + get_form_data(table_name, 'update')
    bd.update_reg(db_data.get_info(table_name), form_data)
    flash(bd.get_message())
    return redirect(f"/index-table/{schema}/{table_name}")

# DELETE

@app.route("/delete/<collection>/<index>/<value>")
def delete(collection, index, value):
    mongo.remove(collection, index, value)
    # flash(bd.get_message())
    return redirect(f"/index-table/{collection}")


def get_form_data(table_name, operation):
    data = []
    table_info = db_data.get_info(table_name)
    for field in bd.select_fields_names(table_info['schema'], table_info['name']):
        if (operation == 'update' and field[0] != table_info['index']) or (operation == 'insert' and (field[0] != 'id' or table_name == 'empleados' or table_name == 'piloto')):
            d = request.form[field[0]]
            try:
                d = int(d)
            except:
                pass
            data.append(d)
    return tuple(data)


if __name__ == '__main__':
    app.run(port=3000, debug=True)
