from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', fila=8, columna=8)

@app.route("/<int:x>")
def filas(x):
    return render_template('index.html', fila=x, columna=8)

@app.route("/<int:x>/<int:y>")
def filas_columnas(x, y):
    return render_template('index.html', fila=x, columna=y)

if __name__ == "__main__":
    app.run(debug=True)