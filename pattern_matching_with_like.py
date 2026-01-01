import sqlite3

def filter_ranges_with_between():
    # Connect to a local SQLite database (example.db)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # SQL query for Challenge #14
    query = "SELECT name, price FROM products WHERE price BETWEEN 30 AND 100"

    cursor.execute(query)
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    filter_ranges_with_between()