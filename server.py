  
import socket               

s = socket.socket()         
host = "192.168.43.24" 
port = 5000
print(host)
s.bind((host, port))        
f = open('gelen.txt','wb')
s.listen(5)                 
while True:
    c, addr = s.accept()     
    print ('Baglanti Aliniyor', addr)
    print ("Aliniyor")
    l = c.recv(1024)
    while (l):
        print ("Aliniyor")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print ("Dosya Alimi Basarili...")
    
    c.close()   
