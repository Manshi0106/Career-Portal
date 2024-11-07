from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(_name_)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the form data
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        email = request.form['email']
        age = request.form['age']
        password = request.form['new-password']
        print(first_name)
        print(last_name)

        # Connect to the database
        conn = sqlite3.connect('prepzoe.db')
        c = conn.cursor()

        # Insert the user into the database
        c.execute('INSERT INTO register (first_name, last_name, email, age, password) VALUES (?, ?, ?, ?, ?)', (first_name, last_name, email, age, password))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Redirect to the login page
        return redirect(url_for('login'))

    # Render the registration form
    return render_template('registeration.html')

@app.route('/login')
def login():
    # Render the login form
    return render_template('login.html')

if _name_ == '_main_':
    app.run(debug=True)