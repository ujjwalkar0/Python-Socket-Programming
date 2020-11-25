import socket
import pickle
a=10
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1024))

while True:
    complete_info = b''
    rec_msg = True
    while True:
        mymsg = s.recv(16)

        if rec_msg:
            print(f"The length of message = {mymsg[:a]}")
            x=int(mymsg[:a])
            rec_msg = False
        complete_info += mymsg
        if (complete_info)-a == x:
            print("Recieved the complete info")
            print(complete_info)
            m=pickle.loads(complete_info)
            print(m)
            rec_msg = True

    print(complete_info) 