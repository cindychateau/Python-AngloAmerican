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
    
    @classmethod
    def muestra_salones(cls):
        query = "SELECT * FROM salones"
        results = connectToMySQL('esquema_salones').query_db(query) #Lista de Diccionarios
        '''results = [
            {"id": 1, "nombre_salon": "Fundamentos de la web"......},
            {"id": 2, "nombre_salon": "Python"......}
            {"id": 3, "nombre_salon": "Java"......}
        ]'''
        #Lista de Objetos Salon
        salones = []
        for salon in results:
            #salon = {"id": 1, "nombre_salon": "Fundamentos de la web"......}
            instancia_salon = cls(salon)
            salones.append(instancia_salon)
        return salones

    

