from flask import Flask
from src.routes.routes import *

app = Flask(__name__)

#Rutas de la app

app.add_url_rule(routes['hello_route'], view_func=routes["Hello_controller"])