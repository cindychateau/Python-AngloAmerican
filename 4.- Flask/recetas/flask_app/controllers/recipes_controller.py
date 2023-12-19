from flask import Flask, render_template, redirect, session, request, flash
from flask_app import app

#MODELOS
from flask_app.models.users import User
from flask_app.models.recipes import Recipe

#RUTAS

#1 ruta para desplegar el formulario (Debemos de revisar que se haya iniciado sesión)
#HTML con el formulario y todos los inputs a guardar
@app.route('/recipes/new')
def recipes_new():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    return render_template('new.html')


#2 ruta para guardar (Debemos de revisar que se haya iniciado sesión)
#Validar la información
#Guarda la info
@app.route('/recipes/create', methods=['POST'])
def recipes_create():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    #Verificar que el formulario esté llenado correctamente
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    
    #Guardar la informacion
    Recipe.save(request.form)
    return redirect('/dashboard')

#/recipes/show/3
@app.route('/recipes/show/<int:id>')
def recipes_show(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    #Llamar a un método que en base al ID me regrese una instancia de receta
    diccionario = {"id": id}
    recipe = Recipe.get_by_id(diccionario)

    return render_template('show.html', recipe=recipe)