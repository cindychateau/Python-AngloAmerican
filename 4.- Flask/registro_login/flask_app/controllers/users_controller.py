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

@app.route('/register', methods=['POST'])
def register():
    #request.form = {"first_name": "Elena", "last_name": "De Troya"...}

    #Validar la info que estamos recibiendo
    if not User.validate_user(request.form):
        #No es válida la info, redireccionamos al formulario
        return redirect('/')    
    
    #Encriptamos la contraseña
    pass_encrypt = bcrypt.generate_password_hash(request.form['password'])
    #Generar un diccionario con toda la info del formulario
    form = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pass_encrypt
    }

    id = User.save(form) #Recibo a cambio el ID del nuevo usuario
    session['user_id'] = id #Guardamos en sesión el identificador del usuario
    return redirect('/dashboard')
    
@app.route('/dashboard')
def dashboard():
    #PENDIENTE: Verificar que el usuario haya iniciado sesión
    return render_template('dashboard.html')