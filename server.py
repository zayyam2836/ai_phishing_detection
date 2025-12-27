# server.py - Simple HTTP Server for Railway
import http.server
import socketserver
import os

PORT = int(os.environ.get('PORT', 8080))

class PhishingDetectorHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Home page
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>🔒 AI Phishing Detector</title>
                <style>
                    body { font-family: Arial; padding: 40px; max-width: 800px; margin: 0 auto; }
                    .container { background: #f0f8ff; padding: 30px; border-radius: 10px; }
                    h1 { color: #2c3e50; }
                    .status { color: green; font-weight: bold; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>✅ AI Phishing Detector - DEPLOYED!</h1>
                    <p class="status">Status: <span style="color:green">● ONLINE</span></p>
                    <p>Your application is successfully running on Railway.</p>
                    <h3>Available Endpoints:</h3>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/health">Health Check</a></li>
                        <li><a href="/api/analyze?url=example.com">Analyze URL</a></li>
                    </ul>
                    <p><em>Phishing detection features will be added soon.</em></p>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
        elif self.path == '/health':
            # Health check endpoint
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = '{"status": "healthy", "service": "AI Phishing Detector", "version": "1.0.0"}'
            self.wfile.write(response.encode())
        elif self.path.startswith('/api/analyze'):
            # Simple API endpoint
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = '{"url": "example.com", "is_phishing": false, "confidence": 0.85}'
            self.wfile.write(response.encode())
        else:
            # Serve static files if they exist
            super().do_GET()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), PhishingDetectorHandler) as httpd:
        print(f"🚀 AI Phishing Detector server running on port {PORT}")
        print(f"🌐 Access at: http://localhost:{PORT}")
        httpd.serve_forever()
