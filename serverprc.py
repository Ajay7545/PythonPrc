import socket
# from socket import *
HOST='' #localhost
PORT=8000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr=s.accept()
print('Connected by ',addr)
while True:
    data=conn.recv(1024)
    print("received",repr(data))
    reply=raw_input("reply :")
    conn.sendall(reply)

conn.close()
