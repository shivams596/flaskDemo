from flask import Flask,request

app = Flask(__name__)
app.config.from_object('config')

from app import views

