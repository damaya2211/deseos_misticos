from flask import Flask
from flask import flash
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import jsonify
from flask import send_from_directory

import os 


app = Flask(__name__)



# Mysql Connection




# settings
app.secret_key = 'abjkhasd22Ht4lEms5289'



   
   
   
   
#principio entrada admin



@app.route('/signup')
def signup():
    return render_template('signup.html')



@app.errorhandler(404)
def page_error(error):
    return render_template("404.html"), 404




# Inicio e Agregar contacto


@app.route('/')
def Index():
        return render_template('index.html')
    

                     
  



#nosotros

@app.route('/nosotros')
def Nosotros():
    return render_template('nosotros.html')



@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

#Fin de nosotros

#inicio index web
@app.route('/inicio')
def Inicio():
    return render_template('inicio.html')


#fin index web


#principio servicios y añadir servicios

@app.route('/servicios')
def servicios():
    return render_template('servicios.html') 



 
 
@app.route('/admin')
def createservicios():
    return render_template('admin.html')
         

#Fin servicios y añadir servicios



# principio contacto
@app.route('/contacto')
def Contacto():
    return render_template('contacto.html')

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

         

#Fin blog y añadir blog



@app.route('/amarre_de_amor')
def amarre():
    return render_template('amarre_de_amor.html')




if __name__=='__main__':
    app.run(port=7000, debug=True)
