# server.py
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
db_file = 'fitness.db'  # Replace with your SQLite database file

def authenticate_user(username, password):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Replace 'users' with the name of your table containing user information
    cursor.execute('SELECT password FROM users WHERE user_id=?', (username,))
    result = cursor.fetchone()

    if result is not None and password == result[0]:
        print("Authentication successful!")
    else:
        print("Authentication failed. Invalid username or password.")

    conn.close()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('user_id')
    password = data.get('user_pswd')

    if username and password:
        result = authenticate_user(username, password)
        if result:
            return jsonify({"message": "Authentication successful!"}), 200
        else:
            return jsonify({"message": "Authentication failed. Invalid username or password."}), 401
    else:
        return jsonify({"message": "Invalid request data."}), 400

if __name__ == '__main__':
    app.run()  # Run the server on localhost, port 5000 by default
