from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    #request.form['strawberry'] = 1
    #request.form['raspberry'] = 2
    #request.form['apple'] = 4
    #request.form['first_name'] = 'Elena'
    #request.form['last_name'] = 'De Troya'
    #request.form['student_id'] = '102030'
    total = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(f'Cobrando a {request.form["first_name"]} por {total} frutas')

    #Correcto: redirect
    return render_template("checkout.html", fresas=request.form['strawberry'], frambuesas=request.form['raspberry'], manzanas=request.form['apple'], nombre=request.form['first_name'], apellido=request.form['last_name'], identificador=request.form['student_id'])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    