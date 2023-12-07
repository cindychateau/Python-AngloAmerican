from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:

    def __init__(self, data):
        #diccionario con toda la información que quiero tener de mi instancia
        self.id = data['id']
        self.nombre_completo = data['nombre_completo']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.salon_id = data['salon_id']

        #Relación con Salón