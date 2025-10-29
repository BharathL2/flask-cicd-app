from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask + MySQL App Running!"

@app.route('/db')
def db_connect():
    try:
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='rootpass',
            database='flaskdb'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        return f"Database connected successfully! Server time: {result}"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
