from flask_app import app

#Importar TODOS nuestros controladores
from flask_app.controllers import users_controller
from flask_app.controllers import messages_controller

#Ejecutamos la app
if __name__ == "__main__":
    app.run(debug=True)