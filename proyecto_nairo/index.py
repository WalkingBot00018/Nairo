from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
# Configura la conexión a la base de datos
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hotel_prueba'

# Inicializa la extensión MySQL
mysql = MySQL(app)



@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/registrar')
def registrar():
    return render_template('registrar.html')

@app.route('/inicioseccion')
def inicioseccion():
    return render_template('inicioseccion.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/adicional', methods=['POST'])
def adicional():
    if request.method == 'POST':
        nro_doc = request.form['nro_doc']   
        nombre_usuario = request.form['nombre_usuario']  
        contrasena = request.form['contrasena']  
        id_rol = request.form['id_rol']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (nro_doc, nombre_usuario, contrasena, id_rol) VALUES (%s, %s, %s, %s)',
                    (nro_doc, nombre_usuario, contrasena, id_rol))  
        mysql.connection.commit()
        return 'registrado'



if __name__ == '__main__':
    app.run(port=5000, debug=True)
