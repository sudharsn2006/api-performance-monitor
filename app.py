from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/logs")
def logs():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM api_logs ORDER BY id DESC LIMIT 50")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
