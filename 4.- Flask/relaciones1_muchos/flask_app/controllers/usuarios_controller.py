from flask import Flask, render_template, request, redirect

from flask_app import app

#Importando los Modelos a utilizar
from flask_app.models.salones import Salon
from flask_app.models.usuarios import Usuario

#Rutas
@app.route('/')
def index():
    #PENDIENTE: Obtener todos los usuarios
    return render_template('index.html') #PENDIENTE: enviar los usuarios

@app.route('/nuevo')
def nuevo():
    #PENDIENTE
    return render_template('nuevo.html')

#PENDIENTE: Ruta que Recibe el formulario y guarda