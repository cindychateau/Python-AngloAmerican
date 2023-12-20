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

    @staticmethod
    def validate_grade(form):
        is_valid = True

        if form['student'] == '':
            flash('Alumno no puede ser vacio', 'grades')
            is_valid = False
        
        if form['grade'] == '': #No se revisa que sea texto
            flash('Ingresa una calificación válida','grades')
            is_valid = False
        else:
            if float(form['grade']) < 1 or float(form['grade']) > 10:
                flash('Calificación debe ser entre 1 y 10', 'grades')
                is_valid = False
        
        if form['date'] == '':
            flash('Ingrese una fecha', 'grades')
            is_valid = False
        else:
            fecha_examen = datetime.strptime(form['date'], '%Y-%m-%d') #Estoy tranformando el texto fecha en formato de fecha
            hoy = datetime.now() #Me da la fecha de hoy 2023-12-20
            if hoy < fecha_examen:
                flash('La fecha no puede ser en el futuro', 'grades')
                is_valid = False
        return is_valid
    
    @classmethod
    def save(cls, form):
        query = "INSERT INTO grades (student, stack, date, grade, belt, user_id) VALUES (%(student)s, %(stack)s, %(date)s, %(grade)s, %(belt)s, %(user_id)s)"
        result = connectToMySQL('esquema_belt_reviewer').query_db(query, form)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM grades"
        results = connectToMySQL('esquema_belt_reviewer').query_db(query) #Lista de Diccionarios
        grades = []
        for grade in results:
            grades.append(cls(grade)) #1.- cls(grade) crea la instancia en base al diccionario. 2.- grades.append() agrego la instancia a la lista
        
        return grades