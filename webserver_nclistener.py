import http.server 
import socketserver
import requests
import threading
import socket
import subprocess

WEB_PORT = 8000
NETCAT_PORT = 1337 

webserver = http.server.SimpleHTTPRequestHandler

def spawn_webserver():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", WEB_PORT), Handler) as httpd:
        print("Server was started at port", WEB_PORT)
        httpd.serve_forever()

        

def spawn_netcatlistener():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as nc:
        nc.bind(('localhost', NETCAT_PORT))
        nc.listen()
        print(f'Netcat listener started at port {NETCAT_PORT}')
        conn, addr = nc.accept()
        with conn:
            print('Connection from ', addr,"\n")
            data = conn.recv(1024)
            print('XXrcvXX:', data.decode())
            while True: 
                user_input = input('> ')
                conn.send(user_input.encode())
                data = conn.recv(1024)
                print("XXrcvXX", data.decode())
    
def main():
    print("Main function")
    t  = threading.Thread(target=spawn_webserver)
    t.start()
    t2 = threading.Thread(target=spawn_netcatlistener())
    t2.start
    #develop function to call for a remote exploit 



if __name__ == '__main__':
    main()

