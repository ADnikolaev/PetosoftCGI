from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("localhost", 7777)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
