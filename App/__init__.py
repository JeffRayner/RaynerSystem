#coding:utf-8
from flask import Flask, session
from datetime import timedelta
from os import urandom

app = Flask(__name__)

#CHAVE DE SEGURANCA
app.secret_key = urandom(12) 

#DEBUG = ON
app.debug = True 

# TEMPO PARA EXPIRAR SESSAO
app.permanent_session_lifetime = timedelta(minutes=10)

# ATUALIZAR SESSAO A CADA SOLICITACAO
app.session_refresh_each_request = True

# IMPORTAR ROTAS
from App.controllers import Routes
