from flask import request
from flask import render_template
from flask import redirect

from flask.views import MethodView

from src.db import db

class IndexController(MethodView):
    
    def get(self):
        with db.cursor() as cur:
            cur.execute('select * from products ')
            data = cur.fetchall()

            cur.execute('select * from categories ')
            categories = cur.fetchall()
            
            return render_template('public/index.html', data=data, categories=categories)

    
    def post(self):
        code = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']
        category_id = request.form['category_id']

        with db.cursor() as cur:
            cur.execute("""insert into products(code, name, stock, value, category_id)
             values(%s, %s, %s, %s, %s)""", 
             (code, name, stock, value, category_id))

            cur.connection.commit()
            return redirect('/')


class DeleteProductController(MethodView):
    def post(self, code):
        with db.cursor() as cur:
            cur.execute('delete from products where code = %s', (code))
            cur.connection.commit()
            return redirect('/')


class UpdateProductController(MethodView):
    def get(self, code):
        with db.cursor() as cur:
            cur.execute('select * from products where code = %s', (code))
            product_data = cur.fetchone()
            return render_template('public/update.html', product_data = product_data)

    def post(self, code):
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']

        with db.cursor() as cur:
            cur.execute('UPDATE products SET name = %s, stock = %s, value = %s WHERE code = %s', ( name, stock, value, code))
            cur.connection.commit()
            return f'editing product {code} works'


class CreateCategoriesController(MethodView):
    
    def get(self):
        with db.cursor() as cur:
            cur.execute('SELECT * FROM categories')
            return render_template('public/categories.html')


    def post(self):
        id = request.form['id']
        name = request.form['name']
        description = request.form['description']

        with db.cursor() as cur:
            cur.execute('insert into categories values(%s, %s, %s)', (id, name, description))
            cur.connection.commit()
            return "Succes"