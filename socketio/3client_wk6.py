import socket

client454 = socket.socket()
host454 = socket.gethostname()
port454 = 9997
client454.connect((host454, port454))

print('Send a mssg to server:')
sendtoserver = input()
client454.send(sendtoserver.encode())
print('\n')
print(client454.recv(1024).decode())
#twishaa sahay ra1911003010068