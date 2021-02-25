import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(hostname= 'Rk server')
port = 80

serversocket.bind(host, port)
serversocket.listen(3)

while True:
    clientsocket, address= serversocket.accept()

    print("Recieved the connection from " % str(address))

    message= "!! Welcome !! to RK's server !!" + "\r\n"
    clientsocket.send(message)
    clientsocket.close()

