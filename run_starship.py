import webview
import threading
import http.server
import socketserver
import os

PORT = 5557
DIRECTORY = r"C:\CREATION\test_site_1"

class ReuseTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    with ReuseTCPServer(("", PORT), Handler) as httpd:
        print(f"Serving Starship GemOS node at http://127.0.0.1:{PORT}/starship_chat.html")
        httpd.serve_forever()

if __name__ == '__main__':
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    window = webview.create_window(
        'Starship GemOS // Bridge & Database Hub',
        f'http://127.0.0.1:{PORT}/starship_chat.html',
        width=1280,
        height=850,
        background_color='#030712',
        resizable=True,
        min_size=(800, 600)
    )
    
    webview.start(gui='edgechromium')