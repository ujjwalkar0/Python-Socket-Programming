import socket

s=socket.socket()
s.bind(("localhost",9000))

s.listen(3)
print("Waiting for connection ...")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connect with ",addr, name)
    c.send(bytes("Welcome to Ujjwl","utf-8"))

