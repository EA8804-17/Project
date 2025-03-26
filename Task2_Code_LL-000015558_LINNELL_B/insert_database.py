import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# Create the products table with all necessary columns
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    description TEXT NOT NULL,
    image TEXT NOT NULL
)
""")

print("Table 'products' created successfully.")

# Insert product data into the products table
products_data = [
    ("Solar panels", "Our solar panels utilize cutting-edge technology to provide efficient, renewable energy solutions.", "/static/assets/solarpanels.png"),
    ("EV charging stations", "Our EV charging stations are reliable, fast, and compatible with all modern electric vehicles.", "/static/assets/evcharging.png"),
    ("Smart home energy management", "Our smart home energy systems optimize electricity usage and provide intelligent device control.", "/static/assets/smarthome.png")
]

cursor.executemany("""
INSERT INTO products (type, description, image)
VALUES (?, ?, ?)
""", products_data)

print("Products inserted successfully.")

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Database operations completed successfully.")
