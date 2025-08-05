🔐 Vulnerable Flask Web App – For Educational Purposes Only
This is a demo Flask web application built to show how common web vulnerabilities can exist in Python apps.

⚠️ Warning: This app is intentionally vulnerable and should NOT be used in production or on public networks.

📦 Features
This web app includes:

Simple login system

Dashboard page

File upload functionality

Object deserialization

SQLite database

It also contains multiple security vulnerabilities for demonstration and testing purposes.

🚧 Known Vulnerabilities
Feature	Vulnerability Type	Description
Login	🔓 SQL Injection	User input is directly injected into SQL queries.
Dashboard	🐞 Cross-Site Scripting (XSS)	Username is not sanitized in HTML rendering.
Upload	📂 Path Traversal	Files can be saved using malicious filenames.
Deserialization	☠️ Insecure Deserialization	Untrusted input is deserialized using pickle.
App Secret Key	🔐 Hardcoded Secret Key	Session security can be compromised.

🛠️ Setup Instructions
1. Install Dependencies
bash
Copy
Edit
pip install flask
2. Run the App
bash
Copy
Edit
python app.py
The app will start at:
http://127.0.0.1:5000

📁 Application Routes
/
Home page with a link to login

/login
Login form

Accepts any username & password

⚠️ SQL Injection possible using inputs like ' OR '1'='1

/dashboard
Displays logged-in user name

⚠️ XSS possible via stored or reflected data

/upload
Uploads a file to ./uploads/ directory

⚠️ Path traversal possible (../../etc/passwd as filename)

/deserialize
Accepts hex-encoded serialized data

⚠️ Insecure deserialization using pickle.loads()

Malicious input can lead to code execution

🧪 Example: SQL Injection
Try logging in with:

vbnet
Copy
Edit
Username: ' OR '1'='1
Password: anything
This will bypass authentication due to SQL injection.

⚠️ Disclaimer
This project is only for:

Educational use

Security research

CTF challenges

Do NOT deploy this app on real servers. It contains serious security flaws that could compromise systems.

✅ How to Fix (Recommendations)
Use parameterized SQL queries

Sanitize all user inputs

Avoid rendering unsanitized data with render_template_string()

Never use pickle with untrusted input

Store secrets in environment variables, not in code

Use secure file saving with werkzeug.utils.secure_filename
