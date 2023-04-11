import http.server 
import socketserver
import requests
import threading
import socket

WEB_PORT = 8080
NETCAT_PORT = 1337 

webserver = http.server.SimpleHTTPRequestHandler

def spawn_webserver():
    print('Web-Server started at', WEB_PORT)

def spawn_netcatlistener():
    print('Netcat Listener started at', NETCAT_PORT)


if __name__ == '__main__':
    main()

