import http.server
import socketserver


if __name__ == "__main__":
    PORT = 8080
    Handler = http.server.SimpleHTTPRequestHandler

    import webbrowser
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        webbrowser.open(f'localhost:{PORT}') #Auto opens up 
        httpd.serve_forever()
