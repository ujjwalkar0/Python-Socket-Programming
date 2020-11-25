import socket
import select

HEADER_LENGTH = 10
IP="127.0.0.1"
PORT = 1456

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET = ipv4, Stock_stream = tcp
s.setsockopt(socket.SQL_SOCKET,socket.SQL_REUSEADDR,1)  #The setsockopt() function provides an application program with the means to control socket behavior. An application program can use setsockopt() to allocate buffer space, control timeouts, or permit socket data broadcasts.

s.bind((IP,PORT))

s.listen()

s_list = []

clients = {}

def receive_message(s):
    try:
        message_header = s.recv(HEADER_LENGTH)

        if not len(message_header):
            return False
        message_length = int(message_header.decode("utf-8").strip())
        return {"header":message_header,"data":s.recv(message_length)}

    except:
        pass

while True:
    read_sockets,_,exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == s:
            client_socket,client_address = s.accept()

            user = receive_message(client_socket)