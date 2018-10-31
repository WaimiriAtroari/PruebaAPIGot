import os
import SimpleHTTPServer
import SocketServer

ip = 'localhost'
port = '8080'
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer((ip, int(port)), Handler)
httpd.serve_forever()