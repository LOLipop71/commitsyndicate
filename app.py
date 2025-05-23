from flask import Flask, jsonify,request
import psycopg2
import os
import json
import logging 

app = Flask(__name__)


gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)


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
    res_idd = request.args.get('id')
    app.logger.info(f"got res_id {res_idd}")
    conn = psycopg2.connect(
        host="aws-0-ap-southeast-1.pooler.supabase.com",
        dbname="postgres",
        user="postgres.slgsuvchudfsllbhuhid",
        password="6wZsZYQpiRNanS_",
        port=5432
    )
    cur = conn.cursor()
    cur.execute(f"SELECT price,description,category,dish_name FROM restaurant_menu_items WHERE res_id = {res_idd};")
    rows = cur.fetchall()
    # Get column names
    columns = [desc[0] for desc in cur.description]
    
    # Convert to list of dicts
    result = [dict(zip(columns, row)) for row in rows]

    # look_up_dict = {"1111":"Ishiro Fusion Bowl Images",
    #                 "1112":"Arnold's Fried Chicken",
    #                 "1113":"Bar Bar Black Sheep",
    #                 "1114":"Encik Tan",
    #                 "1115":"Yardbird Southern Table and Bar"}
    # new_result = []
    # for i in result:
    #     i["restaurant_name"] = look_up_dict[str(res_idd)]
    #     new_result.append(i)
    
    # Convert to JSON string (optional, if you want to print or return)
    json_data = json.dumps(result, indent=2, default=str)

    cur.close()
    conn.close()
    return json_data
