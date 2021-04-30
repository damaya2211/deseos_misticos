from flask import Flask


application = Flask(__name__)


@app.route('/')
def Index():
   return'Hola mUndo'



if __name__=='__main__':
    application.run(debug=True)
