from flask import Flask
import config
from flask import render_template
import socket
import client

UDP_IP = config.LOCAL_DNS_IP
UDP_PORT = config.LOCAL_DNS_PORT

app = Flask(__name__)

#this is the default URL to go to (/)
@app.route("/")
def main(name = None):
    #print "Here is this..." , config.LOCAL_DNS_PORT
    return render_template('index.html')


@app.route("/video1")
def video1():

    #dummy msg of what we're actually doing/what we want from DNS
    MESSAGE = "I need the IP address for |www.herCDN.com|. Please give it to me!"

	
    data = client.talk_to_dns(MESSAGE)
	
    print "Received the IP! it is: ", data

    #we now need to actually use the IP we got from the DNS to direct ourslves to the correct place (wiht a TCP connection)
    resolvedIP = str(data).split(':')[0]
    resolvedPort = str(data).split(':')[1]

    #we don't know the TCP IP/PORT, which is why we're accessing the DNS server to obtain them
    client.tcp(resolvedIP, resolvedPort, 1)

    print("Now going to play the video...")


    #downlod complete, now serving the video...
    return render_template('player.html', video="static/clientdownloads/video1.mp4")


@app.route("/video2")
def video2():

    #dummy msg of what we're actually doing/what we want from DNS
    MESSAGE = "I need the IP address for |www.herCDN.com|. Please give it to me!"

    data = client.talk_to_dns(MESSAGE)


    #we now received the IP that was resolved here. (data = IP address)
    

    print "Received the IP! it is: ", data

    #we now need to actually use the IP we got from the DNS to direct ourslves to the correct place (wiht a TCP connection)
    resolvedIP = str(data).split(':')[0]
    resolvedPort = str(data).split(':')[1]

    client.tcp(resolvedIP, resolvedPort, 2)
    print("Now going to play the video...")

    return render_template('player.html', video="static/clientdownloads/video2.mp4")

@app.route("/video3")
def video3():

    #dummy msg of what we're actually doing/what we want from DNS
    MESSAGE = "I need the IP address for |www.herCDN.com|. Please give it to me!"

    data = client.talk_to_dns(MESSAGE)

    print "Received the IP! it is: ", data

    #we now need to actually use the IP we got from the DNS to direct ourslves to the correct place (wiht a TCP connection)
    resolvedIP = str(data).split(':')[0]
    resolvedPort = str(data).split(':')[1]

    client.tcp(resolvedIP, resolvedPort, 3)
    print("Now going to play the video...")


    #downlod complete, now serving the video...
    return render_template('player.html', video="static/clientdownloads/video3.mp4")

@app.route("/video4")
def video4():

    #dummy msg of what we're actually doing/what we want from DNS
    MESSAGE = "I need the IP address for |www.herCDN.com|. Please give it to me!"

    data = client.talk_to_dns(MESSAGE)

    print "Received the IP! it is: ", data

    #we now need to actually use the IP we got from the DNS to direct ourslves to the correct place (wiht a TCP connection)
    resolvedIP = str(data).split(':')[0]
    resolvedPort = str(data).split(':')[1]

    #we don't know the TCP IP/PORT, which is why we're accessing the DNS server to obtain them
    client.tcp(resolvedIP, resolvedPort, 4)
    print("Now going to play the video...")

    return render_template('player.html', video="static/clientdownloads/video4.mp4")

if __name__ == "__main__":
    app.run(threaded = True)
