import config
import socket



		

def talk_to_dns(MESSAGE):
    UDP_IP = config.LOCAL_DNS_IP
    UDP_PORT = config.LOCAL_DNS_PORT
    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "Sending the message:", MESSAGE

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


    #we now received the IP that was resolved here. (data = IP address)
    data, addr = sock.recvfrom(1024)
    return data
	
	
	
def tcp(resolvedIP, resolvedPort, videoNum):
    BUFFER_SIZE = 1024
    #dummy message of what we're actually doing/what we want from the URL (we want the video)
    MESSAGE = "Please send me the video file |"+str(videoNum)+"|!"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(( resolvedIP, int(resolvedPort) ))
    s.send(MESSAGE)

    #downloading the video
    f = open('static/clientdownloads/video'+str(videoNum)+'.mp4', 'wb')
    data = s.recv(BUFFER_SIZE)
    while(data):
        print "Receiving..."
        f.write(data)
        data = s.recv(BUFFER_SIZE)

    f.close()
    print("Download complete!")
    s.close()