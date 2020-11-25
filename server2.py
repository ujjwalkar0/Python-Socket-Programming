import socket
import _pickle as pickle

a=10
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))  
s.listen(5)

while True:
    clt,adr=s.accept()
    print(f"Connection to {adr} established")

    m = {1:"Client",2:"Server"}

    mymsg = pickle.dumps(m)
    mymsg = bytes(f"{len(mymsg):<{a}}","utf-8") + mymsg

    clt.send(mymsg)   
