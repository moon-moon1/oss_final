from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Cross-Origin Isolation 헤더 추가
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

if __name__ == "__main__":
    port = 8000
    server = HTTPServer(("localhost", port), CORSHandler)
    print(f"Serving at http://localhost:{port}")
    server.serve_forever()
