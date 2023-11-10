#!/usr/bin/python3

import socket

# Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.0.7'
host = socket.gethostbyname()
port = 444

# Binding to socket
serversocket.bind(('192.168.0.7', port)) # Host willl be replaced/substitued with IP, if changed and not running on host

# Stating TCP listener
serversocket.listen(3) # number o connections

while True:
    # Starting the connection
    clientsocket, address = serversocket.accept()
    
    print('receive connection from ' % str(address))

    message = 'Hello! Thank you for connecting to the server. This is an exmple of how sockets can be used' + "\r\n"
    
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
