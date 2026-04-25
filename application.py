from flask import Flask, request, render_template, redirect
from models import db
import models
from models.product import Product
from models.customer import Customer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/add_product', methods=['GET', 'POST'])
def addproduct():
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            category=request.form['category'],
            price=float(request.form['price']),
            quantity=int(request.form['quantity'])
        )
        db.session.add(product)
        db.session.commit()
        return redirect('/products')

    return render_template('addproduct.html')


@app.route('/products')
def view_products():
    products = Product.query.all()
    return render_template('products.html', products=products)


@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def updateproduct(id):
    product = Product.query.get(id)

    if request.method == 'POST':
        product.name = request.form['name']
        product.category = request.form['category']
        product.price = float(request.form['price'])
        product.quantity = int(request.form['quantity'])

        db.session.commit()
        return redirect('/products')

    return render_template('editproduct.html', product=product)


@app.route('/delete_product/<int:id>')
def deleteproduct(id):
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return redirect('/products')


@app.route('/customers')
def viewall():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)


@app.route('/add_customer', methods=['GET', 'POST'])
def addcustomer():
    if request.method == "POST":
        customer = Customer(
            fname=request.form['fname'],
            lname=request.form['lname'],
            email=request.form['email'],
            phone=request.form['phone']
        )

        db.session.add(customer)
        db.session.commit()

        return redirect('/customers')

    return render_template('addcustomer.html')


@app.route('/edit_customer/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    customer = Customer.query.get(id)

    if request.method == 'POST':
        customer.fname = request.form['fname']
        customer.lname = request.form['lname']
        customer.email = request.form['email']
        customer.phone = request.form['phone']

        db.session.commit()
        return redirect('/customers')

    return render_template('editcustomer.html', customer=customer)


@app.route('/delete_customer/<int:id>')
def delete_customer(id):
    customer = Customer.query.get(id)

    db.session.delete(customer)
    db.session.commit()

    return redirect('/customers')


if __name__ == '__main__':
    app.run(debug=False)