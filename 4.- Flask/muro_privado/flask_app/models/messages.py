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

        #2 propiedades extra - Sender Name, Receiver Name (LEFT JOIN)