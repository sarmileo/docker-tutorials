from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Docker Compose Networking, Storage, and Secrets Lab!"

@app.route('/db')
def db_connection():
    db_url = os.getenv("DATABASE_URL", "No DB URL Found")
    return f"Database connection string: {db_url}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)