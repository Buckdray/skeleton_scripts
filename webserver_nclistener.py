import http.server 
import socketserver
import requests
import threading
import socket

WEB_PORT = 8000
NETCAT_PORT = 1337 

webserver = http.server.SimpleHTTPRequestHandler

def spawn_webserver():
    print('Web-Server started at', WEB_PORT)

def spawn_netcatlistener():
    print('Netcat Listener started at', NETCAT_PORT)

def main():
    print("Main function")
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", WEB_PORT), Handler) as httpd:
        print("Server was started at port", WEB_PORT)
        httpd.serve_forever()

if __name__ == '__main__':
    main()

