from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #Encargado de mandar mensajes de error

class Recipe:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        #JOIN
        self.first_name = data['first_name'] #Nombre de la persona que creó la receta
    
    #Valida la receta
    @staticmethod
    def validate_recipe(form):
        is_valid = True

        if len(form['name']) < 3:
            flash('El nombre de la receta debe tener al menos 3 caracteres', 'recipe')
            is_valid = False
        
        if len(form['description']) < 3:
            flash('La descripción debe tener al menos 3 caracteres', 'recipe')
            is_valid = False
        
        if len(form['instructions']) < 3:
            flash('Las instrucciones deben de tener al menos 3 caracteres', 'recipe')
            is_valid = False
        
        if form['date_made'] == "":
            flash('Ingrese una fecha válida', 'recipe')
            is_valid = False
        
        return is_valid

    #Guarde la receta
    @classmethod
    def save(cls, form):
        #form = {"name": "Albondigas", "description": "Deliciosas albondigas de carne", "instructions"......}
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s)"
        result = connectToMySQL('esquema_recetas_aa').query_db(query, form)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT recipes.*, users.first_name FROM recipes JOIN users ON user_id = users.id"
        results = connectToMySQL('esquema_recetas_aa').query_db(query) #Lista de Diccionarios
        recipes = []
        for recipe in results:
            #recipe = diccionario
            recipes.append(cls(recipe)) #1.- cls(recipe) crea la instancia con la info del diccionario. 2.- Agregamos la instancia a la lista de recetas
        return recipes
