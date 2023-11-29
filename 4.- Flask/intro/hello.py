#Terminal: pipenv install flask | python -m pipenv install flask (instala en un ambiente virtual flask)
#Terminal: pipenv shell | python -m pipenv shell (Inicializa mi ambiente virtual) -> exit
#Terminal: python hello.py | python3 hello.py | py hello.py (Ejecutar el archivo) -> CTRL C

from flask import Flask #Importa Flask para permitirnos crear una aplicación web

app = Flask(__name__) #Crea una nueva instancia de la clase Flask

@app.route('/') #Genera una ruta
def hola_mundo(): #Función
    return "¡Hola Mundo!" #Regresa o Despliega el texto de aquí

@app.route('/hola-mundo')
def hola_mundo2():
    return "Esta es otra ruta ¡Hola Mundo!"

#http://127.0.0.1:5000/hola/Cynthia
#nombre = "Cynthia"
@app.route('/hola/<nombre>') #Generamos una ruta '/hola/________'
def hola(nombre):
    return "Hola "+nombre

#http://127.0.0.1:5000/hello/1/Cynthia
@app.route('/hello/<int:numero>/<string:nombre>')
def hello(numero, nombre):
    return "El numero es:"+str(numero)+" el nombre es:"+nombre

if __name__ == "__main__": #Asegura de que el arcchivo se ejecute directamente
    app.run(debug=True) #Ejecuta mi aplicación