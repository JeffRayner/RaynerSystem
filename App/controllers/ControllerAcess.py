from functools import wraps
from flask import redirect, url_for, session
from App.models.Usuarios import Usuario
from App.models.Niveis import Nivel
from App.models.Profile import Profile


def goToPage(Page):
    return redirect(url_for(Page))

def loginRequired(func):
    @wraps(func)
    def decoratorFunc(*args, **kwargs):
        if not isLogged():
            return goToPage("login")
        return func(*args, **kwargs)
    return decoratorFunc

def isLogged():
    if session.get("usuario"):
        return True

def validateLogin(user, senha):
    user = Usuario(Usuario=user, Senha=senha)
    if user.validarLogin():
        session["usuario"] = user.getValues()
    return isLogged()

def islogout():
    if session.get("usuario"):
        del session["usuario"]

def listUsers():
    res = Usuario().listarUsuario()
    if not res:
        goToPage("page_not_found")
    return res

def listNivel():
    res = Nivel().listar()
    if not res:
        goToPage("page_not_found")
    return res

def getUrlProfile(url):
    r = Profile()
    return r.getUsuario(url)