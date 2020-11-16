#coding:utf-8
from flask import Flask, session
from datetime import timedelta

app = Flask(__name__)

app.permanent_session_lifetime = timedelta(minutes=10)
app.session_refresh_each_request = True

from App.controllers import Routes
