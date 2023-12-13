from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

#Importamos todos los modelos
from flask_app.models.users import User

#Importación de BCrypt -> Encriptar la contraseña
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')









@app.route('/dashboard')
def dashboard():
    #PENDIENTE: Verificar que el usuario haya iniciado sesión
    return render_template('dashboard.html')