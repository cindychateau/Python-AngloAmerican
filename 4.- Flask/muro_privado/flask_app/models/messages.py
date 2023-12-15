from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Message:

    def __init__(self, data):
        #data = {"id": 1, "content": "Hola", "created_at":..., "updated_at":..., "receiver_id":1, "sender_id": 5}
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']

        #1 propiedad extra
        self.sender_name = data['sender_name']
    
    @classmethod
    def save(cls, form):
        #form = {"content": "¡Hola!", "sender_id": MI ID, "receiver_id": ID de la persona que recibe}
        query = "INSERT INTO messages (content, sender_id, receiver_id) VALUES(%(content)s, %(sender_id)s, %(receiver_id)s)"
        result = connectToMySQL('esquema_muroprivado').query_db(query, form)
        return result
    
    @classmethod
    def get_my_messages(cls, form):
        #form = {"id": 1}
        query = "SELECT messages.*, users.first_name as sender_name FROM messages JOIN users ON sender_id = users.id WHERE receiver_id = %(id)s"
        results = connectToMySQL('esquema_muroprivado').query_db(query, form) #Lista de diccionarios
        messages = []
        for message in results:
            messages.append(cls(message))
        return messages
    
    @classmethod
    def eliminate(cls, form):
        #form = {"id": 1}
        query = "DELETE FROM messages WHERE id = %(id)s"
        result = connectToMySQL('esquema_muroprivado').query_db(query, form)
        return result