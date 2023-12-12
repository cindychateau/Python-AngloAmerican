#Importaciones
from flask import Flask, render_template, request, redirect, session

#Importar la app
from flask_app import app

#Importando los modelos a utilizar
from flask_app.models.usuarios import Usuario

#Rutas
@app.route('/')
def index():
    usuarios = Usuario.muestra_usuarios() #lista de objetos de usuario que se encuentra en BD
    '''
    [
        OBJUSUARIO. id=1, nombre = "Elena"....,
        OBJUSUARIO. id = 2, nombre = "Juana".....,
        OBJUSUARIO. id = 3 nombre = "Pablo.....
    ]
    '''
    return render_template('index.html', users=usuarios)

@app.route('/nuevo')
def nuevo():
    return render_template('nuevo.html')

@app.route('/crear', methods=['POST'])
def crear():
    #Recibir el formulario.
    #request.form = {"nombre": "Pablo", "apellido": "Picasso", "email": "pablo@cd.com"}
    
    if not Usuario.valida_usuario(request.form): #Si es falso el is_valid
        return redirect('/nuevo') #Mostramos de nuevo el formulario
    else:
        Usuario.guardar(request.form) #Guardamos
    return redirect('/')

#/borrar/1   /borrar/2
@app.route('/borrar/<int:id>')
def borrar(id):
    diccionario = {"id": id} #diccionario = {"id": 2}
    Usuario.borrar(diccionario)
    return redirect('/')

#/editar/1     /editar/2
@app.route('/editar/<int:id>')
def editar(id):
    dicc = {"id": id} #{"id": 1}
    usuario = Usuario.mostrar(dicc) #Instancia de Usuario
    return render_template('editar.html', usuario=usuario)

@app.route('/actualizar', methods=['POST'])
def actualizar():
    #request.form = diccionario con todo lo que el usuario ingresó en el formulario de editar.html
    Usuario.actualizar(request.form)
    return redirect('/')