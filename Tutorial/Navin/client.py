import socket

c=socket.socket()

c.connect(("45.123.15.21",9000))

name = input("Enter Your Name : ")
c.send(bytes(name,"utf-8"))

print(c.recv(1024).decode())
