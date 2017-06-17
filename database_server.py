import socket
import config

TCP_IP = config.HERCDN_DB_HOST
TCP_PORT = config.HERCDN_DB_PORT




BUFFER_SIZE = 1024







while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    conn, addr = s.accept()

    data = conn.recv(BUFFER_SIZE)
    print "Received the message: ", data , "from address: " , addr
    requestedVideo = data.split('|')[1]
    print "They're requesting video: ", requestedVideo

    requestedVideoString = "video" + requestedVideo + ".mp4"
    print "Replying back with ", requestedVideoString, "!"
    if data:
        #sending the video
        videoPath = 'database/' + requestedVideoString
        f = open(videoPath ,'rb')
        frd = f.read(1024)

        while(frd):
            conn.send(frd)
            frd = f.read(1024)
        f.close()
        conn.close()
