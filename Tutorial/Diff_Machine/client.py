import socket
s=socket.socket()

hostname = socket.gethostname()
port = 8500
s.connect((hostname,port))

while True:
    x=raw_input("Enter Message : ")
    s.send(x.encode())
