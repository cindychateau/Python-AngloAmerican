from mysqlconnection import connectToMySQL
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