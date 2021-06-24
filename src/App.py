from flask import Flask, render_template, request, redirect, url_for, flash
from DataBase import DataBase
from DB_data import DB_data
from DataBase_mongo import DataBase_mongo
from copy import deepcopy

bd = DataBase()
db_data = DB_data()

mongo = DataBase_mongo()

app = Flask(__name__)
app.secret_key = "mysecretkey"


@app.route('/')
def index():
    table = {'name':''}
    return render_template('landing-page.html', table = table)


@app.route('/collection/<collection>', methods=['GET', 'POST'])
def index_table(collection):
    data_table = mongo.get_info(collection)
    if request.method == 'GET':

        data_table['data'] = mongo.find(collection)  # PAGINACION

    # Busqueda de registro
    elif request.method == 'POST':
        data = request.form['data']
        field = request.form['field']
        try:
            data = int(data)
        except:
            pass
        try:
            data_table['data'] = mongo.find_many(collection, field, data)
            if not data_table['data']:
                flash(
                    f"ERROR: {collection.capitalize().replace('_', ' ')} ({field.capitalize()}: {data}) Registro inexistente")
                return redirect(f"/collection/{data_table['name']}")
        except:
            flash(f"ERROR: Error producido en la busqueda")
            return redirect(f"/collection/{data_table['name']}")
    # -----

    data_table['edit'] = mongo.enlist_collection(deepcopy(data_table['data']))
    return render_template('collection.html', table=data_table, data_select=mongo.get_data_select(collection))


# INSERTS
@app.route('/insert/<collection>', methods=['POST'])
def insert(collection):
    form_data = get_form_data(collection, 'insert')
    flash('Exito')
    mongo.insert(collection, form_data)
    return redirect(f"/collection/{collection}")


# UPDATES
@app.route('/update/<collection>/<idx>', methods=['POST'])
def update(collection, idx):
    try:
        idx = int(idx)
    except:
        pass
    form_data = get_form_data(collection, 'update')
    print(form_data)
    mongo.update(collection, idx, form_data)
    # flash(bd.get_message())   INSTRUCCION DE UPDATE
    return redirect(f"/collection/{collection}")

# DELETE
@app.route("/delete/<collection>/<index>/<value>")
def delete(collection, index, value):
    mongo.remove(collection, index, value)
    # flash(bd.get_message())
    return redirect(f"/collection/{collection}")


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
    return data


if __name__ == '__main__':
    app.run(port=4000, debug=True)
