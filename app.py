from flask import Flask, jsonify
import psycopg2
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running!"

@app.route('/users')
def get_users():
    conn = psycopg2.connect(
        host="aws-0-ap-southeast-1.pooler.supabase.com",
        dbname="postgres",
        user="postgres.slgsuvchudfsllbhuhid",
        password="6wZsZYQpiRNanS_",
        port=5432
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM restaurant_logins;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)


@app.route('/res_details')
def res_details():
    conn = psycopg2.connect(
        host="aws-0-ap-southeast-1.pooler.supabase.com",
        dbname="postgres",
        user="postgres.slgsuvchudfsllbhuhid",
        password="6wZsZYQpiRNanS_",
        port=5432
    )
    cur = conn.cursor()
    cur.execute("SELECT price,description,category,dish_name FROM restaurant_menu_items WHERE res_id = 1111;")
    rows = cur.fetchall()
    # Get column names
    columns = [desc[0] for desc in cur.description]
    
    # Convert to list of dicts
    result = [dict(zip(columns, row)) for row in rows]
    
    # Convert to JSON string (optional, if you want to print or return)
    json_data = json.dumps(result, indent=2)

    cur.close()
    conn.close()
    return json_data
