from flask import Flask, request, render_template_string, redirect, session
import sqlite3
import os
import pickle
app = Flask(__name__)
app.secret_key = "supersecretkey"  # Hardcoded secret key (⚠️ BAD PRACTICE)
# Database setup (runs only once)
if not os.path.exists("users.db"):
  conn = sqlite3.connect("users.db")
   cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    conn.commit()
    conn.close()
@app.route('/')
def home():
    return "<h1>Welcome to the App</h1><a href='/login'>Login</a>"
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # SQL Injection vulnerability ⚠️
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        if result:
            session['user'] = username
return redirect("/dashboard")
        else:
            return "Invalid credentials!"
    return '''
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input name="password"><br>
            <input type="submit">
        </form>'''
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    # XSS vulnerability ⚠️
    user = session['user']
    return render_template_string(f"<h1>Welcome {user}</h1>")
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        # Path traversal vulnerability ⚠️
        f.save(f"./uploads/{f.filename}")
        return "File uploaded!
    return '''
        <form method="POST" enctype="multipart/form-data">
          Upload file: <input type="file" name="file">
            <input type="submit">
        </form>    '''
@app.route('/deserialize', methods=['POST'])
def deserialize():
    data = request.form['data']
    # Insecure deserialization ⚠️
    obj = pickle.loads(bytes.fromhex(data))
    return f"Deserialized: {obj}"
if __name__ == '__main__':
    app.run(debug=True)
