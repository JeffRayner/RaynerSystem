from App import app
from App.controllers.ControllerAcess import *
from flask import render_template, request, flash, json, jsonify

####################################################################
@app.route("/")
@app.route("/index")
@loginRequired
def main():
    return render_template('index.html')
    
####################################################################
@app.errorhandler(404)
def page_not_found(error):
    return render_template('Error404.html'), 404

####################################################################
@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        validateLogin(request.form['usuario'], request.form['senha'])
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
@loginRequired
def usuarios():
    x = listUsers()
    n = listNivel()
    return render_template( 'usuarios.html', result=x, niveis=n)

####################################################################
@app.route("/<url>")
def profile(url):
    profile = getUrlProfile(url)
    if profile['id']:
        return render_template('page.html', user=profile)
    return page_not_found(404)