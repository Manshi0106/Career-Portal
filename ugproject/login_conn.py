import sqlite3

# Connect to the database
conn = sqlite3.connect('prepzoe.db')

# Create a cursor object
c = conn.cursor()

# Function to check if a user exists in the database
def check_user(username, email, password):
    c.execute("SELECT * FROM login WHERE username=? AND email=? AND password=?", (username, email, password))
    return c.fetchone() is not None
# Close the connection
conn.close()