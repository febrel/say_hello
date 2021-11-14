from flask import Flask, app, render_template, request, flash

app = Flask(__name__)

app.secret_key = "manbearpig_MUDMAN888"

@app.route('/')
def index():
    flash("Cual es tu nombre?")
    return render_template('index.html')

@app.route('/greet', methods=['POST', 'GET'])
def greet():
    flash('Hola '+ str(request.form['name_input']) + ', un saludo para ti!')
    return render_template('index.html')