from flask import Flask
from flask import flash
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import jsonify
from flask import send_from_directory
from flask_mysqldb import MySQL
from datetime import datetime
from flask import abort

import os 


app = Flask(__name__)

login_user = False


# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app) 

CARPETA= os.path.join('uploads/')
app.config['CARPETA']=CARPETA

# settings
app.secret_key = 'mysecretkey'





@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'],nombreFoto)
   
   
   
   
#principio entrada admin



@app.route('/signup')
def signup():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM admin')
    data = cur.fetchall()
    return render_template('signup.html', admin= data)


@app.route("/agregar_admin", methods = ['POST'])
def agregar_admin():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email= request.form['email']
        cargo = request.form['cargo']
        contraseña = request.form['contraseña']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO admin (nombre, email, cargo, contraseña) VALUES (%s, %s, %s, %s)', 
                    (nombre, email, cargo, contraseña))
        
        mysql.connection.commit()
        flash('administrador creado Satisfactoriamente')
        return redirect(url_for('createadmin'))



@app.route('/editad/<id>')
def get_admin(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM admin WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('edit-admin.html',  admin = data[0])




@app.route('/update_admin/<id>', methods = ['POST'])
def update_admin(id):
     if request.method == 'POST':
         nombre = request.form['nombre']
         email = request.form['email']
         cargo = request.form['cargo']
         contraseña = request.form['contraseña']
         cur = mysql.connection.cursor()
         cur.execute(""" 
                     UPDATE admin 
                     SET nombre = %s, 
                     email = %s, 
                     cargo = %s, 
                     contraseña = %s 
                     WHERE id= %s 
                     """, 
                     (nombre, email, cargo, contraseña, id))
         mysql.connection.commit()
         flash('Datos actualizados satisfactoriamente')
         return redirect(url_for('signup'))


@app.route('/delet/<string:id>')
def delet_admin(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM admin WHERE id= {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('signup'))

#Fin admin




@app.errorhandler(404)
def page_error(error):
    return render_template("404.html"), 404






# Inicio e Agregar contacto


@app.route('/')
def Index():
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM contacs')
        data = cur.fetchall()
        return render_template('index.html', contacts= data)
    



@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        mensaje = request.form['mensaje']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacs (fullname, phone, email, mensaje) VALUES (%s, %s, %s, %s)', 
                    (fullname, phone, email, mensaje))
        
        mysql.connection.commit()
        flash('Mensaje Enviado Satisfactoriamente')
        
        return redirect(url_for('Inicio'))


@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacs WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('edit-contact.html',  contact = data[0])
    


@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
     if request.method == 'POST':
         fullname = request.form['fullname']
         phone = request.form['phone']
         email = request.form['email']
         mensaje = request.form['mensaje']
         cur = mysql.connection.cursor()
         cur.execute(""" 
                     UPDATE contacs 
                     SET fullname = %s, phone = %s, 
                     email = %s, mensaje = %s 
                     WHERE id= %s 
                     """, 
                     (fullname, phone, email, mensaje, id))
         mysql.connection.commit()
         flash('Datos actualizados satisfactoriamente')
         return redirect(url_for('Index'))
                     
  
 

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacs WHERE id= {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('Index'))


#fin de inicio y añadir contacto


#nosotros

@app.route('/nosotros')
def Nosotros():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos')
    data = cur.fetchall()
    return render_template('nosotros.html', producto= data)



@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

#Fin de nosotros

#inicio index web
@app.route('/inicio')
def Inicio():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos')
    data = cur.fetchall()
    return render_template('inicio.html', producto= data)


#fin index web


#principio servicios y añadir servicios

@app.route('/servicios')
def servicios():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos')
    data = cur.fetchall()
    return render_template('servicios.html', producto= data)


@app.route('/agregar_servicios', methods = ['POST'])
def agregar_servicios():
    if  request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        foto = request.files['foto']
        
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        
        if foto.filename !='':
            nuevoNombreFoto=tiempo+foto.filename
            foto.save("uploads/"+nuevoNombreFoto)
        
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO productos (nombre, precio, cantidad, foto) VALUES (%s, %s, %s, %s)', 
                    (nombre, precio, cantidad, nuevoNombreFoto))
        
        mysql.connection.commit()
        flash('Servicio subido Satisfactoriamente')
        
        return redirect(url_for('createservicios')) 



@app.route('/editar/<id>')
def get_servicio(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('edit_servicios.html',  producto= data[0]) 



@app.route('/cargar/<id>', methods = ['POST'])
def editar_servicio(id):
     if request.method == 'POST':
         nombre = request.form['nombre']
         precio = request.form['precio']
         cantidad = request.form['cantidad']
         foto = request.files['foto']
         cur = mysql.connection.cursor() 
         cur.execute(""" 
                     UPDATE productos 
                     SET nombre = %s, 
                     precio = %s, 
                     cantidad = %s,
                     foto = %s 
                     WHERE id= %s 
                     """, 
                     (nombre, precio, cantidad, foto, id))
         mysql.connection.commit()
         flash('Datos actualizados satisfactoriamente')
         return redirect(url_for('servicios'))



@app.route('/eliminar/<string:id>')
def eliminar_servicio(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM productos WHERE id= {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('servicios'))


 
 
@app.route('/admin')
def createservicios():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos')
    data = cur.fetchall()
    return render_template('admin.html', producto= data)
         

#Fin servicios y añadir servicios



# principio contacto
@app.route('/contacto')
def Contacto():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacs')
    data = cur.fetchall()
    return render_template('contacto.html', contacts= data)

#fin contacto


#principio calculadora

@app.route('/calculadora', methods=["GET", "POST"])
def calculadora():
    if request.method=="GET":
        return render_template("operar.html")
    else:
        try:
            num1=int(request.form["num1"])
            num2=int(request.form["num2"])
        except:
            abort(404)
        op=request.form["operacion"]
        if op=="sumar":
            resultado=num1+num2
            signo="+"
        elif op=="sumar":
            resultado=num1-num2
            signo="-"
        elif op=="multiplicar":
            resultado=num1*num2
            signo="*"
        elif op=="dividir":
            resultado=num1/num2
            signo="/"
        else:
            abort(404)
        return render_template('operar.html', numero1=num1, numero2=num2, operacion=op, signo=signo, resultado=resultado)
                       
            
            


#fin calculadora






#principio blog y añadir blog

@app.route('/blog')
def blog():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM blog')
    data = cur.fetchall()
    return render_template('blog.html', articulo= data)


@app.route('/agregar_articulo', methods = ['POST'])
def agregar_articulo():
    if request.method == 'POST':
        titulo = request.form['titulo']
        subtitulo = request.form['subtitulo']
        parrafo = request.form['parrafo']
        foto = request.files['foto']
        
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        
        if foto.filename !='':
            nuevoNombreFoto=tiempo+foto.filename
            foto.save("uploads/"+nuevoNombreFoto)
        
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO blog (titulo, subtitulo, parrafo, foto) VALUES (%s, %s, %s, %s)', 
                    (titulo, subtitulo, parrafo, nuevoNombreFoto))
        
        mysql.connection.commit()
        flash('articulo subido Satisfactoriamente')
        
        return redirect(url_for('createblog')) 



@app.route('/edita/<id>')
def get_blog(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM blog WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('edit_blog.html',  articulo = data[0]) 



@app.route('/carga/<id>', methods = ['POST'])
def edit_blog(id):
     if request.method == 'POST':
         titulo = request.form['titulo']
         subtitulo = request.form['subtitulo']
         parrafo = request.form['parrafo']
         foto = request.files['foto']
         cur = mysql.connection.cursor()
         cur.execute(""" 
                     UPDATE blog 
                     SET titulo = %s, 
                     subtitulo = %s, 
                     parrafo = %s,
                     foto = %s 
                     WHERE id= %s 
                     """, 
                     (titulo, subtitulo, parrafo, foto, id))
         mysql.connection.commit()
         flash('Datos actualizados satisfactoriamente')
         return redirect(url_for('blog'))



@app.route('/eliminar/<string:id>')
def eliminar_articulo(id):
    cur = mysql.connection.cursor()
   
    cur.execute("SELECT foto FROM blog WHERE id=%s", id)
    fila = cur.fetchall()
    os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
   
    cur.execute('DELETE FROM blog WHERE id= {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('blog'))


 
 
@app.route('/admin_blog')
def createblog():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM blog')
    data = cur.fetchall()
    return render_template('admin_blog.html', articulo= data)
         

#Fin blog y añadir blog



@app.route('/amarre_de_amor')
def amarre():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacs')
    data = cur.fetchall()
    return render_template('amarre_de_amor.html', contacts= data)




if __name__=='__main__':
    app.run(port=7000, debug=True)