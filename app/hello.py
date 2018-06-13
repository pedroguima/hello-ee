#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import socket

PORT_NUMBER = 9999


class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        if self.path == '/hello':
            self.wfile.write("Hello EE!!")
        elif self.path == '/hostname':
            self.wfile.write(socket.gethostname())
        else:
            self.wfile.write("Nothing's going on")
        return


try:
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port', PORT_NUMBER
    server.serve_forever()

except KeyboardInterrupt:
    print 'Leaving...'
    server.socket.close()
