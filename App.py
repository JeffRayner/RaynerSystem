###################################################
from App import app
from os import urandom
import socket

host = socket.gethostname()
IP = socket.gethostbyname(host)

if __name__ == '__main__':
    app.secret_key = urandom(12)
    #app.run(host= str(IP) , debug=True)
    app.run(debug=True)
