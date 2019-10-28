import socket
import sys

s = socket.socket()
s.connect(('192.168.43.24',5000))
f = open ("D:\Users\user\gonderilecek_dosya", "esse")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()
