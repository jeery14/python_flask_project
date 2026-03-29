from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create DB
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price TEXT
        )
    ''')
    conn.close()

init_db()

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Add product page
@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']

        conn = sqlite3.connect('database.db')
        conn.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
        conn.close()

        return redirect('/products')

    return render_template('add_product.html')

# View products
@app.route('/products')
def view_products():
    conn = sqlite3.connect('database.db')
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()

    return render_template('view_products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)