#Terminal: pipenv install flask | python -m pipenv install flask (instala en un ambiente virtual flask)
#Terminal: pipenv shell | python -m pipenv shell (Inicializa mi ambiente virtual) -> exit
#Terminal: python hello.py | python3 hello.py | py hello.py (Ejecutar el archivo) -> CTRL C

from flask import Flask, render_template #Importa Flask para permitirnos crear una aplicación web. render_template me permite ante una ruta mostrar un html

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

@app.route('/home')
def home():
    return render_template('index.html', nombre="Juana de Arco") #JINJA

#http://127.0.0.1:5000/saluda/Juana/7
#nombre = "Juana"
#cantidad = 7
@app.route('/saluda/<string:nombre>/<int:cantidad>')
def saluda(nombre, cantidad):
    return render_template('saluda.html', name=nombre, num=cantidad)

if __name__ == "__main__": #Asegura de que el arcchivo se ejecute directamente
    app.run(debug=True) #Ejecuta mi aplicación