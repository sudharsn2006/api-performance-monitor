import requests, time, sqlite3

# List of APIs to monitor
API_LIST = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/users",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/albums",
    "https://jsonplaceholder.typicode.com/todos"
]

# Monitoring loop
while True:
    for API_URL in API_LIST:
        start = time.time()
        try:
            r = requests.get(API_URL, timeout=10)
            response_time = time.time() - start
            status = r.status_code
            error = None
        except Exception as e:
            response_time = None
            status = None
            error = str(e)

        # Store in SQLite
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO api_logs(api_url, status_code, response_time, error)
            VALUES (?, ?, ?, ?)
        """, (API_URL, status, response_time, error))
        conn.commit()
        conn.close()

        print("Logged:", API_URL, status, response_time)

    # Wait 10 seconds before next round
    time.sleep(10)
