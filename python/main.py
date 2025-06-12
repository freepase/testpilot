import logging
from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[logging.StreamHandler()]
)

@app.get("/")
def index():
    return "- lone wolf capital webhook -"


@app.route('/', methods=['POST'])
def post():
    # Log raw body (e.g., JSON, text)
    body = request.get_data(as_text=True)  # returns str, not bytes
    app.logger.info(f"Received POST body: {body}")

    # Optionally, parse as JSON
    json_body = request.get_json(silent=True)
    if json_body:
        app.logger.info(f"Parsed JSON: {json_body}")

    return "OK", 200


if __name__ == "__main__":
    # Dev only: run "python main.py" and open http://localhost:8080
    app.run(host="localhost", port=8080, debug=True)
