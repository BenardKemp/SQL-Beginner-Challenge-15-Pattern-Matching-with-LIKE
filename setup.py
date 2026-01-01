import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, " \
"name TEXT, " \
"category TEXT, " \
"price NUMBER )")



cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (101, 'Wireless Mouse', 'Accessories', 24.99)")
cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (102, 'Mechanical Keyboard', 'Accessories', 89.00)")
cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (103, '27-inch Monitor', 'Displays', 299.99)")
cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (104, 'USB-C Hub', 'Accessories', 34.50)")
cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (105, 'Laptop Stand', 'Workspace', 39.90)")
cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (106, 'Webcam', 'Accessiores', 59.90)")


conn.commit()
conn.close()