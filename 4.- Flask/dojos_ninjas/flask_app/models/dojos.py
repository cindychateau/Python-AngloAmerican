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

    

