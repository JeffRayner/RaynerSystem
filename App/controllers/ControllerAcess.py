from functools import wraps
from flask import redirect, url_for, session
from App.models import Model

def loginRequired(func):
    @wraps(func)
    def decoratorFunc(*args, **kwargs):
        if not session.get("usuario"):
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    return decoratorFunc

def goToPage(Page):
    return redirect(url_for(Page))

def validateLogin(user, senha):
    user = Model.User(name=user, passw=senha)
    if user.checkLogin():
        session["usuario"] = user.getValues()
        return user.getValues()

def listUsers():
    value = Model.User().getUserList()
    res = []
    for L in value:
        res.append({"Id":L[0],"Name":L[1],"Level":L[2],"Email":L[3],"Date":L[4]})
    return res