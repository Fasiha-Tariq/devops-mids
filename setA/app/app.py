import os
from flask import Flask  # type: ignore[reportMissingImports]
import redis  # type: ignore[reportMissingImports]

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=6379, decode_responses=True)


@app.route("/")
def home():
    return f"Hello from DevOps Mid {os.environ.get('ROLLNO', 'unknown')}"


@app.route("/visit")
def visit():
    count = r.incr("visits")
    return f"Visit count: {count}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
