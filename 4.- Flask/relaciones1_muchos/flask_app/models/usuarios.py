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
        self.nombre_salon = data['nombre_salon']
    
    @classmethod
    def guardar_usuario(cls, formulario):
        #formulario = diccionario con la info
        query = "INSERT INTO usuarios (nombre_completo, email, salon_id) VALUES (%(nombre_completo)s, %(email)s, %(salon_id)s)"
        result = connectToMySQL('esquema_salones').query_db(query, formulario)
        return result
    
    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT usuarios.*, nombre_salon FROM usuarios JOIN salones ON salon_id = salones.id ORDER BY nombre_completo"
        results = connectToMySQL('esquema_salones').query_db(query) #Lista de Diccionarios
        usuarios = []
        for usuario in results:
            usuarios.append(cls(usuario))
        return usuarios