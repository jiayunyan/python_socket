import struct
from socket import *
import time
import os

udpSocket = socket(AF_INET, SOCK_DGRAM)

requestFileData = struct.pack("!H8sb5sb",1,"test.txt".encode("utf-8"),0,"octet".encode("utf-8"),0)
udpSocket.sendto(requestFileData, ("192.168.56.1", 69))
udpSocket.close()