# API Performance Monitor

## Description
Python project to track API response times, HTTP status codes, and errors. Data is stored in SQLite and visualized in Grafana.

## Features
- Monitor multiple APIs dynamically
- Store logs in SQLite
- Flask API to expose logs
- Grafana dashboard for visualization
- Track errors, slow response times, and API performance trends

## Technologies
- Python (Flask, Requests, SQLite)
- Grafana (Dashboard JSON included)

## Setup Instructions
1.**Clone the repo:**

   git clone https://github.com/<YourUsername>/api-performance-monitor.git

2.**Install dependencies:**

pip install -r requirements.txt

3.**Create database:**

python db_setup.py


4.**Run monitor:**

python monitor.py


5.**Start Flask API:**

python app.py
