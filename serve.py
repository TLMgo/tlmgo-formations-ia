#!/usr/bin/env python3
"""
Local server for Formations IA presentations.

Usage:
    python serve.py              # default: localhost:8080
    python serve.py 9000         # custom port
    python serve.py 0.0.0.0 9000 # bind all interfaces
"""
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

host = sys.argv[1] if len(sys.argv) > 1 else "localhost"
port = int(sys.argv[2]) if len(sys.argv) > 2 else 8080

print(f"Serving at http://{host}:{port}")
print("Press Ctrl+C to stop.\n")

server = HTTPServer((host, port), SimpleHTTPRequestHandler)
webbrowser.open(f"http://{host}:{port}")
server.serve_forever()
