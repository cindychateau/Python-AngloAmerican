from flask import Flask, render_template, redirect, session, request, flash
from flask_app import app

from flask_app.models.users import User
from flask_app.models.grades import Grade

@app.route('/new/grade')
def new_grade():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    return render_template('new.html')

@app.route('/create/grade', methods=['POST'])
def create_grade():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    #Validar la Calificación
    if not Grade.validate_grade(request.form):
        return redirect('/new/grade')
    
    #Guardar la Calificación
    Grade.save(request.form)

    return redirect('/dashboard')