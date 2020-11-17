from App import app
from App.controllers.ControllerAcess import *
from flask import render_template, request, flash, session,json, jsonify, make_response


####################################################################

@app.errorhandler(404)
def page_not_found(error):
    return render_template('Error404.html'), 404

####################################################################

@app.route("/")
@app.route("/index")
@loginRequired
def main():
    return render_template('index.html')

####################################################################

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        validateLogin(request.form['usuario'], request.form['senha'])
        if session.get("usuario"):
            return goToPage("main")
        else:
            flash("Login Inválido !")

    if session.get("usuario"):
        return goToPage("main")

    return render_template('login.html')

####################################################################

@app.route('/logout')
def logout():
    if session.get("usuario"):
        del session["usuario"]
    return goToPage("main")

####################################################################

@app.route('/teste', methods=['GET'])
def teste():
    x = listUsers()
    return render_template( 'usuarios.html', result=x)



