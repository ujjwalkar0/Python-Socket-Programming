import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))  # This methode is uuseful when server and client are same computer or device
s.listen(5)

while True:
    clt,adr=s.accept()
    print(f"Connection to {adr} established")
    clt.send(bytes("Socket is a Programming in Python here","utf-8"))
    clt.close()