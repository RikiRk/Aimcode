import socket  
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(input('Enter the site to get a ip '))
print(ip)
