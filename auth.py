from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import bcrypt

app = Flask(__name__)
CORS(app)

# Create database
def init_db():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()


# REGISTER
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data["username"]
    password = data["password"]

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    try:
        conn = sqlite3.connect("users.db")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, hashed)
        )

        conn.commit()
        conn.close()

        return jsonify({"message": "User registered successfully"})

    except:
        return jsonify({"message": "User already exists"})


# LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("SELECT password FROM users WHERE username=?", (username,))
    user = cur.fetchone()

    conn.close()

    if user and bcrypt.checkpw(password.encode(), user[0]):
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"})


if __name__ == "__main__":
    app.run(debug=True)