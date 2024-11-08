# app.py
from flask import Flask, render_template, jsonify
import threading
import processor  # Starts the processor as a separate thread

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # Serve the HTML page

@app.route('/api/data')
def get_data():
    # Endpoint for getting data to the frontend via AJAX
    return jsonify({"message": "Hello from Flask API!"})

if __name__ == "__main__":
    # Start the processor in a background thread
    processor_thread = threading.Thread(target=processor.run_processor, daemon=True)
    processor_thread.start()
    app.run(host="0.0.0.0", port=3000)
