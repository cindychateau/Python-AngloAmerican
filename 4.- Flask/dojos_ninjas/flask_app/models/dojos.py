from flask_app.config.mysqlconnection import connectToMySQL
from .ninjas import Ninja #Importando la clase Ninja

class Dojo:

    def __init__(self, data):
        #data = {id: 1, name: "Colombia", created_at:"0000-00-00", updated_at:"0000-00-00"}
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        #Una lista con todos los ninjas
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('esquema_dojos_ninjas').query_db(query) #Lista de Diccionarios
        #results = [
        #    {id: 1, name: "Colombia", created_at:"0000-00-00", updated_at:"0000-00-00"}
        #    {id: 2, name: "México", created_at:"0000-00-00", updated_at:"0000-00-00"}
        #    {id: 3, name: "Perú", created_at:"0000-00-00", updated_at:"0000-00-00"}
        #]
        dojos = []
        for d in results:
            #d = {id: 1, name: "Colombia", created_at:"0000-00-00", updated_at:"0000-00-00"}
            dojos.append(cls(d)) #cls(d) -> Crea una instancia de Dojo. append agrega la instancia a mi lista de dojos
        return dojos
    
    @classmethod
    def save(cls, formulario):
        #formulario = {"name": "Chile"}
        #Query = Consulta de BD
        query = "INSERT INTO dojos (name) VALUES (%(name)s)" #-> INSERT INTO dojos (name) VALUES ('Chile')
        result = connectToMySQL('esquema_dojos_ninjas').query_db(query, formulario)
        return result

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        #data = {"id": 1}
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        results = connectToMySQL('esquema_dojos_ninjas').query_db(query, data) #Lista de Diccionarios
        #POR DEF vamos a tener 1 registro
        dojo = cls(results[0]) #Creamos instancia de Dojo
        #dojo.ninjas = []
        for row in results:
            ninja = {
                'id': row['ninjas.id'], #
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
                'dojo_id': row['dojo_id']
            }
            instancia_ninja = Ninja(ninja)
            dojo.ninjas.append(instancia_ninja)
        return dojo
