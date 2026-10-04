from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        app = os.environ.get("APP", "LMS")
        message = f"Hello, {app} \nPath: {self.path} \n"
        self.wfile.write(message.encode())

port = int(os.getenv("PORT", 8000))
server = HTTPServer(('', port), Handler)
print(f'Server started at {port}')
server.serve_forever()