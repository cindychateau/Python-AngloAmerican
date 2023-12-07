from flask_app.config.mysqlconnection import connectToMySQL

class Salon:

    def __init__(self, data):
        #data = {"id": 1, "nombre_salon": "Python", "created_at":......}
        self.id = data['id']
        self.nombre_salon = data['nombre_salon']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #No se utiliza hoy (Relación con Usuario)
        self.usuarios = []
    

