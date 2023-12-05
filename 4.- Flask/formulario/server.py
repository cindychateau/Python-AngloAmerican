from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "llave secreta." #establece una clave/llave secreta para dar más seguridad a nuestras cookies, que es donde se guarda la sesión

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    #request.form = {
    #   "nombre": "Elena de Troya"    
    #   "email": "elena@codingdojo.com",
    #   "tipo_usuario": "normal"   
    #}
    print(request.form)
    #return "Info recibida."+request.form['nombre']

    session['usuario'] = request.form['nombre']
    session['correo'] = request.form['email']

    return redirect("/exito")

@app.route("/exito")
def exito():
    return render_template("exito.html")

if __name__ == "__main__":
    app.run(debug=True)