from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add_product():
    name = request.form['name']
    price = float(request.form['price'])
    new_product = Product(name=name, price=price)
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:product_id>', methods=['POST'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return "Product not found."

    product.name = request.form['name']
    product.price = float(request.form['price'])
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:product_id>')
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return "Product not found."

    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():  # Set up the application context
        db.create_all()
    app.run()
