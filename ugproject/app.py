from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567890",
    database="prepzoe"
)

# Create a cursor object
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('newlogin.html')

# Route to render login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check login credentials against the database
        cursor.execute("SELECT * FROM users WHERE username=%s, email=%s AND password=%s", (username,email, password))
        user = cursor.fetchone()

        if user:
            # Login successful, redirect to a dashboard or home page
            return redirect(url_for('home'))
        else:
            # Login failed, render login page with an error message
            return render_template('newlogin.html', error='Invalid username or password')

    # Render the login page
    return render_template('newlogin.html')

# Route to render signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        confirm = request.form['confirm']

        # Insert new user into the database
        cursor.execute("INSERT INTO users (fullname, username, email, phone, password, confirm) VALUES (%s, %s, %s, %s, %s, %s)", (fullname, username, email, phone, password, confirm))
        db.commit()

        # Redirect to the login page after successful signup
        return redirect(url_for('newlogin.html'))

    # Render the signup page
    return render_template('newlogin.html')

# Route for the dashboard or home page
@app.route('/home')
def dashboard():
    return render_template("prepzone.html")

if __name__ == '__main__':
    app.run(debug=True)