from flask import Flask
from flask import flash


app = Flask(__name__)



@app.route('/')
def Index():
   return'Hola mUndo'



if __name__=='__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
