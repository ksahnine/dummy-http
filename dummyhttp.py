#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser

import sys
import socket

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        self.send_response(200)
        self.send_header("Content-type", "plain/text")
        self.end_headers()
        hostname = socket.gethostbyname(socket.gethostname())
        self.wfile.write("Hi! I'm [" + sys.argv[1] + "] service from " + hostname + "\n")
        
    do_POST = do_GET
    do_PUT = do_POST
    do_DELETE = do_GET
        
def main():
    port = 8080
    print('Listening on port:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()
 
if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Dummy HTTP server which returns a given message parameter.\n"
                    "Example:\n"
                    "   ./dummyhttp.py <message>")
    (options, args) = parser.parse_args()
    
    main()
