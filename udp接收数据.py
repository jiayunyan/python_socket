# -*- coding: utf-8 -*-
from socket import *
udpSocket=socket(AF_INET,SOCK_DGRAM)
sendAddr=('192.168.42.1',8080)

udpSocket.sendto(b"hahahah",('192.168.42.1',8080))
udpSocket.close()