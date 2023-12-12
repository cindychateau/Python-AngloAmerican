from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #Importamos flash para mandar mensajes de validación
class Usuario:

    def __init__(self, data):
        #diccionario -> data = {"id": 1, "nombre":"Elena", "apellido":"De Troya"....}
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM usuarios"
        results = connectToMySQL('esquema_usuarios_aa').query_db(query) #lista de diccionarios
        '''[
            {"id": 1, "nombre":"Elena", "apellido":"De Troya"....},
            {"id": 2, "nombre":"Juana", "apellido":"De Arco"....},
        ]'''
        usuarios = []
        #pasamos de lista de diccionarios a convertirla en lista de objetos 
        for u in results:
            #u = {"id": 1, "nombre":"Elena", "apellido":"De Troya"....}
            usuario = cls(u) #usuario = Usuario(u) -> usuario.id = 1, usuario.nombre = "Elena" Una INSTANCIA de usuario con la info de BD
            usuarios.append(usuario)
        
        return usuarios #lista de objetos
    
    @classmethod
    def guardar(cls, formulario):
        #formulario = {"nombre": "Pablo", "apellido": "Picasso", "email": "pablo@codingdojo.com"}
        query = "INSERT INTO usuarios (nombre, apellido, email) VALUES (%(nombre)s, %(apellido)s, %(email)s)"
        result = connectToMySQL('esquema_usuarios_aa').query_db(query, formulario) #ID del nuevo registro
        return result
    
    @classmethod
    def borrar(cls, diccionario):
        #diccionario = {"id": 1}
        query = "DELETE FROM usuarios WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuarios_aa').query_db(query, diccionario)
        return result
    
    @classmethod
    def mostrar(cls, diccionario):
        #diccionario = {"id": 1}
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuarios_aa').query_db(query, diccionario) #Lista de Diccionarios
        '''
        [
            {"id": 1, "nombre":"Elena", "apellido":"De Troya"......}
        ]
        '''
        usuario = cls(result[0])
        return usuario

    #UPDATE usuarios SET nombre = 'Elena'..... WHERE id = 1
    @classmethod
    def actualizar(cls, formulario):
        #formulario = {"id": 1, "nombre": "Elena", "apellido": "De Troya"...}
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s WHERE id=%(id)s"
        result = connectToMySQL('esquema_usuarios_aa').query_db(query, formulario)
        return result
    
    @staticmethod
    def valida_usuario(formulario):
        is_valid = True #Asumimos que todo en el formulario del usuario es correcto

        if len(formulario['nombre']) < 3:
            flash('Nombre debe tener al menos 3 caracteres', 'registro')
            is_valid = False
        
        if len(formulario['apellido']) < 3:
            flash('Apellido debe de tener al menos 3 caracteres', 'registro')
            is_valid = False

        #Consultar si ya existe ese email en la bd
        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        results = connectToMySQL('esquema_usuarios_aa').query_db(query, formulario) #Lista de Diccionarios
        if len(results) >= 1: #SI EXISTE ya un usuario con ese correo
            flash('E-mail registrado previamente', 'registro')
            is_valid = False
        
        #PENDIENTE validar email -> ER
        
        return is_valid
        
        