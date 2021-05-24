import socket

sob454 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ho454 = socket.gethostname()
po454 = 9997
sob454.bind((ho454, po454))
sob454.listen(6)
print("I am the server!")

while True:
    conn454, ad454 = sob454.accept()
    sentbyclient = conn454.recv(1024).decode()
    if sentbyclient == 'ping' or sentbyclient == 'PING':
        sentbyserver = 'SERVER: Pong!'
        conn454.send(sentbyserver.encode())
    else:
        sentbyserv = 'SERVER: DROPPED!!!'
        conn454.send(sentbyserv.encode())
    conn454.close()
    #twishaa sahay ra1911003010068