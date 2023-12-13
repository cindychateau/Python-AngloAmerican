#Importar la conexión con la BD
from flask_app.config.mysqlconnection import connectToMySQL

import re #Importación de Expresiones Regulares
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email

from flask import flash #flash es el encargado de mostrar errores/mensajes

class User:

    def __init__(self, data):
        #data = {diccionario con toda la info que tiene la instancia}
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, form):
        #form = {"first_name": "Elena", "last_name": "De Troya", "email": "elena@cd.com", "password": "YA ESTE ENCRIPTADO"}
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL('esquema_login').query_db(query, form)
        return result #El ID de nuevo registro que se realizó
    
    #PENDIENTE: Validar la info que recibimos en el formulario