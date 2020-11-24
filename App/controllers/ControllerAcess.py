from functools import wraps
from flask import redirect, url_for, session
from App.models import Model


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
    user = Model.User(name=user, passw=senha)
    if user.checkLogin():
        session["usuario"] = user.getDictValues()
    return isLogged()

def islogout():
    if session.get("usuario"):
        del session["usuario"]

def listUsers():
    res = Model.User().getUserList()
    if not res:
        goToPage("page_not_found")
    return res