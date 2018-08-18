import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("pythonprogramming.net",8000))
sock.listen(2)
(client,(ip,port))=sock.accept()