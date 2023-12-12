#Importar flask
from flask import Flask

#inicializacion app
app = Flask(__name__)

#Declaramos llave secreta
app.secret_key = "La llave super secreta"