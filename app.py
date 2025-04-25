from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'supercutesecret'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart=cart_items)

@app.route('/add_to_cart/<int:item_id>')
def add_to_cart(item_id):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM items WHERE id = ?', (item_id,)).fetchone()
    conn.close()
    
    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append({'id': item['id'], 'name': item['name'], 'price': item['price']})
    return redirect(url_for('index'))

@app.route('/purchase')
def purchase():
    session.pop('cart', None)
    return '<h2>Thank you for your purchase! 💖</h2>'

if __name__ == '__main__':
    app.run(debug=True)