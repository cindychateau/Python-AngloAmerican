#Importación de flask_app
from flask_app import app

#Importar controladores
from flask_app.controllers import usuarios_controller

#Ejecutar mi app
if __name__=="__main__":
    app.run(debug=True)