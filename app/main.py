from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            with open('file.json', 'r') as file:
                content = file.read()
            
            self.wfile.write(content.encode())
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        if self.path == '/':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            # Handle both form data and JSON input
            try:
                params = json.loads(post_data)
            except json.JSONDecodeError:
                params = parse_qs(post_data)
            
            if 'link' in params:
                link = params['link'][0] if isinstance(params['link'], list) else params['link']
                
                try:
                    with open('file.json', 'r+') as file:
                        try:
                            data = json.load(file)
                        except json.JSONDecodeError:
                            data = []
                        
                        if not isinstance(data, list):
                            data = []
                        
                        data.append(link)
                        
                        file.seek(0)
                        json.dump(data, file)
                        file.truncate()
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write("Link added successfully".encode())
                except Exception as e:
                    self.send_error(500, f"Internal Server Error: {str(e)}")
            else:
                self.send_error(400, "Bad Request: 'link' parameter is missing")
        else:
            self.send_error(404, "Not Found")
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on 0.0.0.0:{port}")
    httpd.serve_forever()
    
if __name__ == '__main__':
    run()