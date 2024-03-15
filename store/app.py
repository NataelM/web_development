from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#inicializar instancia de la aplicacion
app = Flask(__name__)
# dirección de la base de datos         # nombre de la base 'store.bd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['ALCHEMY_TRACK_MODIFICATIONS'] = False
# se inicializa la base de datos
db = SQLAlchemy(app)

# crear el modelo de la base de datos
class Product(db.Model): # se crea la tabla producto
    # atributos de la tabla
    id       = db.Column(db.Integer, primary_key = True)
    name     = db.Column(db.String(80), nullable = False)
    price    = db.Column(db.Float, nullable = True)
    quantity = db.Column(db.Integer, nullable = True)

    def __repr__(self):
        return f'<Product {self.name} available {self.quantity}>'



############################ rutas

# pagina principal
@app.route('/')
def index():
    return render_template('index.html')

# crear producto
@app.route('/add', methods = ['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # recolectando info a la base de datos
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']
        # agregar un producto a la bd
        new_product = Product(name = name,
                            price = price,
                            quantity = quantity,
                            )
        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('list_products'))
    return render_template('add_products.html')

# leer los productos
@app.route('/catalog')
def list_products():
    products = Product.query.all()
    return render_template('list_products.html', products = products)

# actualizar los productos
@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update_product(id):
    # buscar el producto, si no lo encuentra manda error
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        # preguntamos por los atributos del product
        product.name = request.form['name']
        product.price = request.form['price']
        product.quantity = request.form['quantity']
        db.session.commit()

        return redirect(url_for('list_products'))
    return render_template('update_product.html', product = product)

#eliminar productos
@app.route('/delete/<int:id>')
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('list_products'))

@app.route('/client')
def client():
    products = Product.query.all()
    return render_template('client.html', products = products)

# correr la app
if __name__ == '__main__':
    app.run(debug = True)