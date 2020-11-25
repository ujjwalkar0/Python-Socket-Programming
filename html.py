import socket
import time
import pickle

def create():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET = ipv4, Stock_stream = tcp
    try:
        s.bind(('localhost',9001))  # 1234 --> PORT Number   ## The bind() method of Python's socket class assigns an IP address and a port number to a socket instance. The bind() method is used when a socket needs to be made a server socket. As server programs listen on published ports, it is required that a port and the IP address to be assigned explicitly to a server socket.
        s.listen(5) # listen --> It listens for connections from clients.  A listening socket does just what it sounds like. It listens for connections from clients. When a client connects, the server calls accept() to accept, or complete, the connection. The client calls connect() to establish a connection to the server and initiate the three-way handshake.
        while True:
            clientsocket,address = s.accept()
            rd=clientsocket.recv(5000).decode()

            pieces = rd.split('\n')

            if (len(pieces)>0):
                print(pieces[0])
            
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += """
            <html>
            <title>Hello</title>
            <body>
            <h1>Hello World</h1>
            </body>
            </html>

            """

            clientsocket.sendall(data.encode())
            clientsocket.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt :
        print("\nShut Down\n")
    except Exception as exc:
        print("Error\n")
        print(exc)
    s.close()
print("Access http://localhost:9001")
create()