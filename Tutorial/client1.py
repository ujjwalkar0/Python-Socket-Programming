import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET = ipv4, Stock_stream = tcp

s.connect((socket.gethostname(),1235))  #Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server

# msg = s.recv(1024)  


full_msg = ''

while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")
print(full_msg)