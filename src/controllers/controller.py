from flask import request
from flask import render_template
from flask import redirect

from flask.views import MethodView

from src.db import db

class IndexController(MethodView):
    
    def get(self):
        return "Hello world"

    
    def post(self):
        code = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']
        category_id = request.form['category_id']

        print(code, name, stock, value, category_id)
        return "method post is works"