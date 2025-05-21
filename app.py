from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running!"

@app.route('/users')
def get_users():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        port=5432
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)
