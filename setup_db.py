import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create items table
c.execute("""
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    image TEXT
)
""")

# Insert cute example items
items = [
    ('Moon Mug', 12.99, 'https://i.imgur.com/abc123.png'),
    ('Star Pillow', 18.50, 'https://i.imgur.com/def456.png'),
    ('Galaxy Socks', 8.25, 'https://i.imgur.com/ghi789.png')
]

c.executemany('INSERT INTO items (name, price, image) VALUES (?, ?, ?)', items)
conn.commit()
conn.close()