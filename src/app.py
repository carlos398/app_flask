from flask import Flask
from src.routes.routes import *

app = Flask(__name__)

#Rutas de la app
app.add_url_rule(routes['index_route'], view_func=routes["index_controller"])

#ruta error 404
app.register_error_handler(routes['not_found_route'], routes["not_found_controller"])