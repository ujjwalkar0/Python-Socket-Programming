import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET = ipv4, Stock_stream = tcp

s.bind((socket.gethostname(),1235))  # 1234 --> PORT Number   ## The bind() method of Python's socket class assigns an IP address and a port number to a socket instance. The bind() method is used when a socket needs to be made a server socket. As server programs listen on published ports, it is required that a port and the IP address to be assigned explicitly to a server socket.

s.listen(5) # listen --> It listens for connections from clients.  A listening socket does just what it sounds like. It listens for connections from clients. When a client connects, the server calls accept() to accept, or complete, the connection. The client calls connect() to establish a connection to the server and initiate the three-way handshake.

while True:
    clientsocket,address = s.accept()
    print(f"Connection from {address} established !")
    clientsocket.send(bytes("Welcome to the server !","utf-8"))
    clientsocket.close()