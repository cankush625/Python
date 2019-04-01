import socket

host = 'localhost'
port = 6767

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host, port))

print("Server listening to the port : ", port)

s.listen(1)

c, addr = s.accept()

filename = c.recv(1024)

try :
    f = open(filename, 'rb')
    content = f.read()
    c.send(content)
    f.close()
except FileExistsError :
    c.send(b"File dose not exist!!!")

c.close()

'''By Ankush Chavan'''