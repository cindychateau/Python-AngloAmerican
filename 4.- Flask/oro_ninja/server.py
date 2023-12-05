from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = "llave super secreta"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    #Guardar en sesion la cantidad de monedas.
    #session['monedas']
    #Si NO existe en mi sesion monedas, significa que es la primera vez que juego
    if 'monedas' not in session:
        session['monedas'] = 0
    
    if 'actividades' not in session:
        session['actividades'] = []
    
    #request.form = {
    #   "edificio": "granja" o "cueva" o "casa" o "casino"    
    #}
    cantidad_monedas = 0
    if request.form['edificio'] == 'granja':
        #Gana entre 10-20
        cantidad_monedas = random.randint(10, 20)
    elif request.form['edificio'] == 'cueva':
        #Ganar 5-10
        cantidad_monedas = random.randint(5, 10)
    elif request.form['edificio'] == 'casa':
        #Ganar 2-5
        cantidad_monedas = random.randint(2, 5)
    else: #es casino
        #gana o pierde entre 0-50
        cantidad_monedas = random.randint(-50, 50)
    
    session['monedas'] += cantidad_monedas
    session['actividades'].append('Se obtuvieron:'+str(cantidad_monedas)+' en:'+request.form['edificio'])

    #session['actividades'] = [
    #   'Se obtuvieron 3 en casa',   
    #   'Se obtuvieron 5 en cueva',   
    #   'Se obtuvieron -10 en casino',   
    #]

    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)