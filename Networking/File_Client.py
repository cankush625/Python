import socket

s = socket.socket()

s.connect(('localhost', 6767))

filename = input("Enter a filename : ")

s.send(filename.encode())

content = s.recv(1024)

print(content.decode())

s.close()

'''By Ankush Chavan'''