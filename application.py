from flask import Flask, request, render_template, redirect
from models import db
import models
from models.product import Product

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

@app.route('/add_product', methods=['GET', 'POST'])
def addproduct():
    if request.method == 'POST':
        product = Product(
            name = request.form['name'],
            cat = request.form['category'],
            price = float(request.form['price']),
            quantity = int(request.form['quantity'])
        )
        db.session.add(product)
        db.session.commit()
        return redirect('/products')
    
    return render_template('addproduct.html')

if __name__ == '__main__':
    app.run(debug=False)