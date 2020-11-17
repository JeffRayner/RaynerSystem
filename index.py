"""from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Home Page Route - nice work Andrew!!!'
"""

###################################################
from App import app
from os import urandom

#import socket
#host = socket.gethostname()
#IP = socket.gethostbyname(host)

app.secret_key = urandom(12)