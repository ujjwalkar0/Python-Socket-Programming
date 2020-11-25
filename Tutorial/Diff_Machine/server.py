import socket
import time

listensocket = socket.socket()
Port = 8500
maxCon = 999
IP = socket.gethostname()

listensocket.bind(('',Port))

listensocket.listen(maxCon)

print("Server Started At "+ IP + "on Port "+str(Port))
clientsocket,address = listensocket.accept()

print("New Connection made !")

running = True

while running:
    message = clientsocket.recv(1024).decode()