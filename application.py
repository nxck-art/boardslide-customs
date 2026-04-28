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

#routes

#HOME PAGE
@app.route('/')
def homepage():
    return "<h1>Welcome to our most dope website!</h1>"

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def addproduct():
    if request.method == 'POST':
        product = Product
        product.name = request.form['name']
        product.category = request.form['category']
        product.price = float(request.form['price'])
        product.quantity = int(request.form['quantity'])
        product.image_url = request.form['image_url']

        db.session.add(product)
        db.session.commit()
        return redirect('/products')
    
    return render_template('addproduct.html')

@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def updateproduct(id):
    product = Product.query.get(id)
    if product is None:
        return redirect('/products')
    if request.method == 'POST':
        product.name = request.form['name']
        product.category = request.form['category']
        product.price = float(request.form['price'])
        product.quantity = int(request.form['quantity'])
        product.image_url = request.form['image_url']

        db.session.commit()
        return redirect('/products')
    return render_template('editproduct.html', product=product)

@app.route('/delete_product/<int:id>')
def deleteproduct():
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return redirect('/products')

#customer management
@app.route('/customers')
def viewall():
    customers = Customer.query.all()
    return render_template('customers.html', customers = customers)

@app.route('/add_customer', methods=['GET', 'POST'])
def addcustomer():
    if request.method == "POST":
        customer = Customer()
        customer.fname = request.form['fname']
        customer.lname = request.form['lname']
        customer.email = request.form['email']
        customer.phone = request.form['phone']


        db.session.add(customer)
        db.session.commit()

        return redirect('/customers')
    return render_template('addcustomer.html')

@app.route('/build_skateboard')
def build_skateboard():
    return render_template('build_skateboard.html')

# Products to add to database
with app.app_context():

    db.create_all()

    if Product.query.count() == 0:

        p1 = Product()
        p1.name = "Element Complete Skateboard"
        p1.category = "Complete Skateboards"
        p1.price = 79.99
        p1.quantity = 5
        p1.image_url = "images/element_complete.jpg"

        p2 = Product()
        p2.name = "Santa Cruz Deck 8.0"
        p2.category = "Decks"
        p2.price = 59.99
        p2.quantity = 8
        p2.image_url = "images/santa_cruz_deck.jpg"

        p3 = Product()
        p3.name = "Independent Trucks Stage 11"
        p3.category = "Trucks"
        p3.price = 64.99
        p3.quantity = 6
        p3.image_url = "images/independent_trucks.jpg"

        p4 = Product()
        p4.name = "Spitfire Wheels 52mm"
        p4.category = "Wheels"
        p4.price = 39.99
        p4.quantity = 10
        p4.image_url = "images/spitfire_wheels.jpg"

        p5 = Product()
        p5.name = "Bones Reds Bearings"
        p5.category = "Bearings"
        p5.price = 19.99
        p5.quantity = 12
        p5.image_url = "images/bones_reds_bearings.jpg"

        p6 = Product()
        p6.name = "Mob Grip Tape"
        p6.category = "Grip Tape"
        p6.price = 9.99
        p6.quantity = 15
        p6.image_url = "images/mob_grip_tape.jpg"

        p7 = Product()
        p7.name = "Thrasher Hoodie"
        p7.category = "Clothing"
        p7.price = 59.99
        p7.quantity = 4
        p7.image_url = "images/thrasher_hoodie.jpg"

        p8 = Product()
        p8.name = "Vans Skate Shoes"
        p8.category = "Shoes"
        p8.price = 69.99
        p8.quantity = 7
        p8.image_url = "images/vans_skate_shoes.jpg"

        db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8])
        db.session.commit()

        print("Products added!")

if __name__ == '__main__':
    app.run(debug=False)