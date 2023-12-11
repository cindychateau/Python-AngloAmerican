from flask import Flask, redirect, request, render_template
from flask_app import app

#Modelos
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    lista_dojos = Dojo.get_all() #Lista instancias de Dojo
    return render_template('index.html', dojos=lista_dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    #request.form = {"name": "Chile"}
    Dojo.save(request.form)
    return redirect('/dojos')

#Mostrar el formulario
@app.route('/new/ninja')
def new_ninja():
    lista_dojos = Dojo.get_all() #Lista instancias de Dojo
    return render_template('new.html', dojos=lista_dojos)

#Recibir formulario
@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    #request.form = {"first_name":"Elena", "last_name": "De Troya", "age":18, "dojo_id": 1}
    Ninja.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {"id": id}
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template('dojo.html', dojo=dojo)