from flask_app.config.mysqlconnection import connectToMySQL #Conexión con BD
from flask import flash #flash es el encargado de mandar mensajes/errores
from datetime import datetime #Manipular fechas y saber la fecha actual

class Grade:

    def __init__(self, data):
        self.id = data['id']
        self.student = data['student']
        self.stack = data['stack']
        self.date = data['date']
        self.grade = data['grade']
        self.belt = data['belt']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
