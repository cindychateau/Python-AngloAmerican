from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    #request.form = {
    #   "nombre": "Elena de Troya"    
    #   "email": "elena@codingdojo.com"    
    #}
    print(request.form)
    #return "Info recibida."+request.form['nombre']
    return redirect("/exito")

@app.route("/exito")
def exito():
    return render_template("exito.html")

if __name__ == "__main__":
    app.run(debug=True)