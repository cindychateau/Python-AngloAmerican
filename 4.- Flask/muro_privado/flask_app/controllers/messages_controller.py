from flask import Flask, render_template, redirect, session, request, flash
from flask_app import app

from flask_app.models.messages import Message

@app.route('/send_message', methods=['POST'])
def send_message():
    #Recibimos request.form = {"content": "¡Hola!", "sender_id": MI ID, "receiver_id": ID de la persona que recibe}
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect('/')
    
    #Guardamos el mensaje -> Método que reciba el formulario y guarde
    Message.save(request.form)
    return redirect('/dashboard')

@app.route('/delete_message/<int:id>') #en mi URL obtengo el ID del mensaje a borrar
def delete_message(id):
    form = {"id": id}
    #Función que elimine el mensaje
    Message.eliminate(form)
    return redirect('/dashboard')