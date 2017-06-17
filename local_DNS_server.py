import socket
import config

UDP_IP = config.LOCAL_DNS_IP
UDP_PORT = config.LOCAL_DNS_PORT



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




#name value type
#type should be A
#this is where the IP resolve happens, make an array containin these values, then based on the msg return the appropriate ip



#Local dummy DNS contacts dummy DNS for hiscinema.com with record of type V.
#DNS server for hiscinema.com sends reply with IP address of authoritative dummy DNS for herCDN. This is a NS type.

#Local dummy DNS sends query to dummy DNS herCDN.com
#Dummy DNS for herCDN.com replies to local dummy DNS with a Type=A record.


#Local dummy DNS replies to the client with resolved IP address of content server.




while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if data:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.sendto(data, (config.HISCINEMA_COM_HOST, config.HISCINEMA_COM_PORT))

        data, addr2 = sock.recvfrom(1024)
		
        sock.sendto(data, (config.HERCDN_COM_HOST, config.HERCDN_COM_PORT))
        data3, addr3 = sock.recvfrom(1024)
		
        print "Local DNS data received!: ", data, addr
        
        sock.sendto(data, addr)
		