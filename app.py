from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' # Change this to a strong, random key!

# --- Routes ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # --- IMPORTANT: In a real application, you would connect to a database
        # to verify username and password. This is just a placeholder. ---
        if username == 'user' and password == 'password': # Placeholder credentials
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
        else:
            # --- IMPORTANT: In a real application, you would store this
            # user information securely in a database. This is a placeholder. ---
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/contactus', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # You can print/store/send this data as needed
        print(f"Message from {name} ({email}): {message}")
        return "Thank you for contacting us!"
    return render_template('contactus.html')


if __name__ == '__main__':
    app.run(debug=True) # debug=True allows for automatic reloading and helpful error messages