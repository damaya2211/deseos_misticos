from flask import Flask, request


application = app = Flask(__name__)


@app.route('/')
def Index():
   return'Hola mUndo'



if __name__=='__main__':
    app.run(debug=True)
