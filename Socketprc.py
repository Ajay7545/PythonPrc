import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)
server='pythonprogramming.net'
port=80
serverip=socket.gethostbyname(server)
print(serverip)
req="GET / HTTP/1.1\n Host: "+server+"\n\n"
s.connect((server,port))
s.send(req.encode())
result=s.recv(4096)
#print(result)
while(len(result)>0):
    print(result)
    result=s.recv(1024)

