#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 80

httpd = HTTPServer(('',port), CGIHTTPRequestHandler)
print('Starting simple httpd on port:' + str(httpd.server_port))
httpd.serve_forever()
