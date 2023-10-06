from flask import Flask,render_template, request, redirect, url_for, 
from flask_mysqldb  import mysql


app = Flask(__name__)
app.config['']
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/registrar')
def registrar():
    return render_template('registrar.html')

@app.route('/inicioseccion')
def inicioseccion():
    return render_template('inicioseccion.html')

@app.route('/juegos')
def juegos():
    return render_template('juegos.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
