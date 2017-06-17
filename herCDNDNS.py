import socket
import config

IP = config.HERCDN_COM_HOST
PORT = config.HERCDN_COM_PORT

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((IP, PORT))


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if data:
        data = str(config.HERCDN_DB_HOST)+":"+str(config.HERCDN_DB_PORT)
        print "Her CDNDNS sending: " + data
        sock.sendto(str(data).encode(), addr)