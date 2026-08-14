import http.server
import socketserver

PORT = 5557
DIRECTORY = r"C:\CREATION\test_site_1"

class ReuseTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == '__main__':
    with ReuseTCPServer(("", PORT), Handler) as httpd:
        print(f"Starship Bridge online at: http://127.0.0.1:{PORT}/starship_chat.html")
        httpd.serve_forever()