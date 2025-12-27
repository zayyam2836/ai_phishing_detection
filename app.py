# app.py - SIMPLEST VERSION
from flask import Flask

# Create Flask app
app = Flask(__name__)

# Single route
@app.route('/')
def hello():
    return "✅ AI Phishing Detector is LIVE!"

# Health check
@app.route('/health')
def health():
    return "🟢 Healthy"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
