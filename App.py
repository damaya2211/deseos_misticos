from flask import Flask
from flask import flash
from flask import redirect
from flask import url_for
from flask import render_template


app = Flask(__name__)



@app.route('/')
def Index():
   return render_template('index.html')
    

                    

#nosotros

@app.route('/nosotros')
def Nosotros():
   return render_template('nosotros.html')



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



         

#Fin servicios y añadir servicios



# principio contacto
@app.route('/contacto')
def Contacto():
   return render_template('contacto.html')

#fin contacto




#principio blog y añadir blog

@app.route('/blog')
def blog():
   return render_template('blog.html', articulo= data)

         

#Fin blog y añadir blog



@app.route('/amarre_de_amor')
def amarre():
    return render_template('amarre_de_amor.html')




if __name__=='__main__':
    app.run(host="0.0.0.0" port=80, debug=True)
