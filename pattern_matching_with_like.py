import sqlite3

def pattern_matching_like():
    # Connect to a local SQLite database (example.db)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # SQL query for Challenge #15
    query = "SELECT name, price FROM products WHERE name LIKE '%USB%'"

    cursor.execute(query)
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    pattern_matching_like()