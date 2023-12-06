from flask import Flask, render_template, request, redirect
from user import Usuario #Importano la clase User para poder utilizar sus funciones

app = Flask(__name__)

#Crear una ruta que despliegue TODOS los usuarios
@app.route('/')
def index():
    usuarios = Usuario.muestra_usuarios() #lista de objetos de usuario que se encuentra en BD
    return render_template('index.html', users=usuarios)

@app.route('/nuevo')
def nuevo():
    return render_template('nuevo.html')

@app.route('/crear', methods=['POST'])
def crear():
    #Recibir el formulario.
    #request.form = {"nombre": "Pablo", "apellido": "Picasso", "email": "pablo@cd.com"}
    Usuario.guardar(request.form)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)