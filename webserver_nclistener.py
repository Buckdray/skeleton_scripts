import http.server 
import socketserver
import requests
import threading
import socket

WEB_PORT = 8000
NETCAT_PORT = 1337 

webserver = http.server.SimpleHTTPRequestHandler

def spawn_webserver():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", WEB_PORT), Handler) as httpd:
        print("Server was started at port", WEB_PORT)
        httpd.serve_forever()

        

def spawn_netcatlistener():
    print('Netcat Listener started at', NETCAT_PORT)

def main():
    print("Main function")
    t= threading.Thread(target=spawn_webserver)
    t.start()
    //spawn_netcatlistener()


if __name__ == '__main__':
    main()

