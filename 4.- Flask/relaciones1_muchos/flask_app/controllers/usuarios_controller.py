from flask import Flask, render_template, request, redirect

from flask_app import app

#Importando los Modelos a utilizar
from flask_app.models.salones import Salon
from flask_app.models.usuarios import Usuario

#Rutas
@app.route('/')
def index():
    #Obtener todos los usuarios
    usuarios = Usuario.muestra_usuarios()
    return render_template('index.html', usuarios=usuarios) #enviar los usuarios

#Formulario: 2 rutas. 1.- MOSTRAR formulario. 2.- Recibir la info y guardarla
@app.route('/nuevo')
def nuevo():
    #Obtener todos los salones. Lista
    salones = Salon.muestra_salones() #Lista de instancias de salón
    return render_template('nuevo.html', salones=salones)

#Ruta que Recibe el formulario y guarda
@app.route('/guardar', methods=['POST'])
def guardar():
    #Recibimos request.form = {"nombre_completo": "Elena de Troya", "email": "elena@cd.com", "salon_id": 1}
    #Guardar el nuevo registro
    Usuario.guardar_usuario(request.form)
    return redirect('/')