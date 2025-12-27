from flask import Flask, request, jsonify
import sys
sys.path.append('.')
import main  # Import your existing CLI logic

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>AI Phishing Detector</h1>
    <p>API is running. Use /analyze?url=example.com</p>
    '''

@app.route('/analyze')
def analyze():
    url = request.args.get('url', '')
    if not url:
        return jsonify({'error': 'No URL provided'})
    
    # Call your existing logic from main.py
    # For now, return demo response
    return jsonify({
        'url': url,
        'status': 'analyzed',
        'phishing': 'login' in url.lower()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
