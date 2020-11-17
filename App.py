###################################################
#from App import app
from os import urandom
from flask import Flask

app = Flask(__name__)
app.secret_key = urandom(12)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
if __name__ == '__main__':
    
    #app.run(host= str(IP) , debug=True)
    app.run(debug=True)