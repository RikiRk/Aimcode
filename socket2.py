import socket 
import time
s = socket.socket()
a=0
print ("Socket successfully created ")

port = 1234
s.bind(('',port))
print("The server binded with",port)
s.listen(5)
print ("The socket is listening ")

while True:
    clientsocket,addr = s.accept()
    print ("Got connection from ", addr)
    txt = " !! WARM WELCOME !!          " 
    clientsocket.send(txt.encode('utf-8'))
    while a<10:
        a=a+1
        time.sleep(1)
        print(a) 
    txt2 = " FUCK YOU AND GET LOST "   
    clientsocket.send(txt2.encode('utf-8'))
    clientsocket.close()

