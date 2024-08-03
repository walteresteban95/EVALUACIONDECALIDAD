import psycopg2

# Connect to your PostgreSQL database on a remote server
conn = psycopg2.connect(host="5.199.162.56", port="5432", dbname="test_erp", user="postgres", password="test123")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a test query
cur.execute("SELECT * FROM clients")

# Retrieve query results
records = cur.fetchall()

# Finally, you may print the output to the console or use it anyway you like
print(records)
