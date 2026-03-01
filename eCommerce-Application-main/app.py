from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)
DB_FILE = "ecommerce.db"

# ----- Database Setup ----- #
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity INTEGER,
            customer_name TEXT,
            customer_email TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ----- Helper Functions ----- #
def get_all_products():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "price": row[3],
            "stock": row[4]
        })
    return products

def add_product(name, description, price, stock):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, description, price, stock) VALUES (?, ?, ?, ?)",
                   (name, description, price, stock))
    conn.commit()
    conn.close()

# ----- Routes ----- #
@app.route('/')
def index():
    products = get_all_products()
    return render_template('index.html', products=products)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        stock = int(request.form['stock'])
        add_product(name, description, price, stock)
        return redirect(url_for('admin'))
    products = get_all_products()
    return render_template('admin.html', products=products)

@app.route('/export_json')
def export_json():
    products = get_all_products()
    return jsonify(products)

# ----- Main ----- #
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
