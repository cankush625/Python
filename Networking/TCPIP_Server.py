import socket

host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host, port))

print("Server listening to the port : ", port)

s.listen(1)

c, addr = s.accept()
print("Connection from : ",str(addr))

c.send(b"Hello Im Ankush")
c.send("Bye".encode())
c.close()

'''By Ankush Chavan'''