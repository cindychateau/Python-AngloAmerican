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
