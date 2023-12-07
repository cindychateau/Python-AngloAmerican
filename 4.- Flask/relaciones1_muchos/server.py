#Importación de APP
from flask_app import app

#Importación Controladores
from flask_app.controllers import usuarios_controller

#Ejecución de APP
if __name__ == "__main__":
    app.run(debug=True)