from http.server import BaseHTTPRequestHandler, HTTPServer


def get_greeting():
    return "Welcome to EFD Python project!"


def get_page():
    return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>EFD Python Welcome</title>
    <style>
        :root {{ --bg: #062c1d; --panel: #ffffff; --accent: #16a34a; --text: #0f172a; --muted: #64748b; }}
        * {{ box-sizing: border-box; }}
        body {{ margin: 0; font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(135deg, var(--bg), #0d4a2c); color: var(--text); min-height: 100vh; display: grid; place-items: center; padding: 24px; }}
        .card {{ background: var(--panel); border-radius: 20px; padding: 2.5rem 3rem; box-shadow: 0 20px 50px rgba(0,0,0,0.25); text-align: center; max-width: 560px; width: 100%; }}
        .badge {{ display: inline-block; padding: 0.4rem 0.8rem; border-radius: 999px; background: rgba(22,163,74,0.12); color: var(--accent); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; font-size: 0.8rem; margin-bottom: 1rem; }}
        h1 {{ margin: 0 0 0.75rem; font-size: 2rem; color: var(--accent); }}
        p {{ margin: 0; color: var(--muted); line-height: 1.6; }}
    </style>
</head>
<body>
    <div class=\"card\">
        <div class=\"badge\">EFD • Python</div>
        <h1>{get_greeting()}</h1>
        <p>This polished welcome page is served from the Python project and is ready to be viewed in a browser.</p>
    </div>
</body>
</html>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(get_page().encode("utf-8"))


def start_server(port=8080):
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Server started at http://localhost:{port}/")
    server.serve_forever()


if __name__ == "__main__":
    start_server()
