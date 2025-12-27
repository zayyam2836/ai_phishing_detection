#!/usr/bin/env python3
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = int(os.environ.get('PORT', 3000))

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>AI Phishing Detector</title>
                <style>
                    body { font-family: Arial, sans-serif; padding: 40px; max-width: 800px; margin: 0 auto; }
                    .container { background: #f0f8ff; padding: 30px; border-radius: 10px; }
                    .success { color: green; }
                    .online { color: green; font-weight: bold; }
                    ul { line-height: 1.8; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1 class="success">✅ AI Phishing Detector - DEPLOYED!</h1>
                    
                    <p><strong>Status:</strong> <span class="online">● ONLINE</span></p>
                    <p>Your application is successfully running on Railway.</p>
                    
                    <h3>Available Endpoints:</h3>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/health">Health Check</a></li>
                        <li><a href="/api/analyze?url=example.com">Analyze URL</a></li>
                    </ul>
                    
                    <p><em>Phishing detection features will be added soon.</em></p>
                    
                    <hr>
                    <p><strong>Deployment Details:</strong></p>
                    <ul>
                        <li>Platform: Railway.app</li>
                        <li>Python: """ + sys.version.split()[0] + """</li>
                        <li>Port: """ + str(PORT) + """</li>
                    </ul>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "healthy", "service": "AI Phishing Detector"}')
        elif self.path.startswith('/api/analyze'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Simple mock analysis
            self.wfile.write(b'{"url": "example.com", "is_phishing": false, "confidence": 0.85}')
        else:
            super().do_GET()

if __name__ == '__main__':
    print(f"🚀 AI Phishing Detector running on port {PORT}")
    httpd = HTTPServer(('', PORT), Handler)
    httpd.serve_forever()
