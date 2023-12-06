#pipenv install pymysql flask

from flask import Flask, render_template, redirect, session, request

from mysqlconnection import connectToMySQL #Importa el archivo que hace mi conexión con MySQL

app = Flask(__name__)

app.secret_key = "Esta es la llave secreta"

#Creamos una ruta para ingresar un nuevo registro
@app.route('/nuevo')
def nuevo():
    data = {
        "nombre": "Juana",
        "apellido": "De Arco",
        "email": "juana@codingdojo.com"
    }

    #Interpolacion: %(LLAVE)s
    query = "INSERT INTO usuarios (nombre, apellido, email) VALUES ( %(nombre)s, %(apellido)s, %(email)s )" # INSERT INTO usuarios (nombre, apellido, email) VALUES ('Elena', 'De Troya', 'elena@codingdojo.com')
    result = connectToMySQL('esquema_usuarios_aa').query_db(query, data) #Recibimos el ID del nuevo registro
    return data['nombre']+" registrada."+str(result) #result = 1

@app.route('/')
def index():
    query = "SELECT * FROM usuarios"
    results = connectToMySQL('esquema_usuarios_aa').query_db(query) #Recibo una lista de diccionarios
    return results

#INSERT -> recibimos el ID nuevo generado
#SELECT -> Lista de Diccionarios
#UPDATE o DELETE -> NO RECIBO NADA
#Problemas -> Recibo FALSE


if __name__ == "__main__":
    app.run(debug=True)