from App import app
from App.controllers.ControllerAcess import *
from flask import render_template, request, flash,json, jsonify


####################################################################

@app.errorhandler(404)
def page_not_found(error):
    return render_template('Error404.html'), 404

####################################################################

@app.route("/")
@loginRequired
def main():
    return render_template('index.html')

####################################################################

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        if validateLogin(request.form['usuario'], request.form['senha']):
            return goToPage("main")
        else:
            flash("Login Inválido !")

    if isLogged():
        return goToPage("main")

    return render_template('login.html')

####################################################################

@app.route('/logout')
def logout():
    islogout()
    return goToPage("main")

####################################################################

@app.route('/usuarios', methods=['GET'])
def usuarios():
    x = listUsers()
    return render_template( 'usuarios.html', result=x)