from flask import Flask
from flask import flash
from flask import redirect
from flask import url_for
from flask import render_template


app = Flask(__name__)



@app.route('/')
def Index():
   return render_template('index.html')



if __name__=='__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
