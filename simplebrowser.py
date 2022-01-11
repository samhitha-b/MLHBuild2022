import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
#encode is to encode it in UTF-8 because python uses unicode
mysock.send(cmd)

while True:
    data = mysock.recv(512) #receives 512 characters
    if len(data) < 1:
        break #if nothing is recieved
    print(data.decode(), end='')

mysock.close()