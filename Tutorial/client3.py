import socket
import pickle
HEADERSIZE = 10


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET = ipv4, Stock_stream = tcp
s.connect((socket.gethostname(),1235))  #Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"New Message length : {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg=False

        full_msg += msg  #.decode("utf-8")

        if len(full_msg) == msglen+HEADERSIZE:
            print("Full msg recieved")
            # print(full_msg[HEADERSIZE:])

            d=pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            # new_msg = True
            # full_msg = ''

    print(full_msg)