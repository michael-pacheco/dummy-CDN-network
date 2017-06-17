import socket
import config

hisCinStr = str(config.HISCINEMA_COM_HOST)+':'+str(config.HISCINEMA_COM_PORT)
herCDNStr = str(config.HERCDN_DB_HOST)+':'+str(config.HERCDN_DB_PORT)
dnsList = []
dns1 = ['www.hiscinema.com', hisCinStr, 'A']
dnsList.append(dns1)
dns2 = ['hiscinema.com', 'www.hisCinema.com', 'NS']
dnsList.append(dns2)

dns3 = ['www.herCDN.com', herCDNStr, 'A']
dnsList.append(dns3)
dns4 = ['herCDN.com', 'www.herCDN.com', 'NS']
dnsList.append(dns4)

UDP_IP = config.HISCINEMA_COM_HOST
UDP_PORT = config.HISCINEMA_COM_PORT

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if data:
        neededIP = data.split('|')[1]
        print "Received message:", data, "From address: ", addr
        print "It needs to resolve the IP for: ", neededIP, " - looking it up in the DNS"
        for record in dnsList:
            if record[0] == str(neededIP) and record[2] == 'A':
                resolvedIP = record[1]
        print "The resolved IP is:", resolvedIP , "replying back with it."
        sock.sendto(str(resolvedIP).encode(), addr)