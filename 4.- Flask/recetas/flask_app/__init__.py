from flask import Flask #Importamos Flask

app = Flask(__name__) #Inicializamos app

app.secret_key = "Llave seeeecreeetaaaaaa!" #Se necesita para la sesión, es la manera en que se encripta

app.config['UPLOAD_FOLDER'] = 'flask_app/static/img'