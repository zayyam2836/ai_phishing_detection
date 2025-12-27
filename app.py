# app.py - MINIMAL WORKING FLASK APP
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>AI Phishing Detector</title></head>
    <body style="font-family: Arial; padding: 40px;">
        <h1>✅ AI Phishing Detector - DEPLOYED!</h1>
        <p>Your Flask app is successfully running on Railway.</p>
        <p><a href="/health">Health Check</a> | <a href="/demo">Demo</a></p>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy", "service": "AI Phishing Detector"}

@app.route('/demo')
def demo():
    return "Demo page - Phishing detection will be added here"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
