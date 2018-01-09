#coding:utf-8

import socket
import sys
import time

#HOST = '119.23.220.55'
HOST ='106.14.122.104'
# HOST =""
PORT = 8000
ADDR =(HOST,PORT)
BUFSIZE = 1024

MONEY="0.01"

print "check api"
sock = socket.socket()
try:
    a = sock.connect(ADDR)
except Exception,e:
    print 'error',e
    sock.close()
    sys.exit()

print 'have connected with server'


data="#REQ_ORDER_ID#"+MONEY
if len(data)>0:
    print 'send:',data
    sock.sendall(data) #不要用send()
    recv_data = sock.recv(BUFSIZE)
    ID=recv_data
    print recv_data
    sock.close()
sock.close()

time.sleep(1)

print "check api2"
sock = socket.socket()
try:
    a = sock.connect(ADDR)
except Exception,e:
    print 'error',e
    sock.close()
    sys.exit()

print 'have connected with server'

data="#REQ_CODE#"+ID
if len(data)>0:
    print 'send:',data
    sock.sendall(data) #不要用send()
    recv_data = sock.recv(BUFSIZE)
    img=recv_data
    file = file("./temp.png", "wb")
    try:
        file.write(img)
    finally:
        file.close()
    print "save img..."
    sock.close()
sock.close()


for cnt in range(100):
    time.sleep(3)
    print "check api3==>"+str(cnt)
    sock = socket.socket()
    try:
        a = sock.connect(ADDR)
    except Exception,e:
        print 'error',e
        sock.close()
        sys.exit()
    print 'have connected with server'
    data="#CHECK_STA#"+ID
    if len(data)>0:
        print 'send:',data
        sock.sendall(data) #不要用send()
        recv_data = sock.recv(BUFSIZE)
        # print recv_data
        if(recv_data=='Y'):
            print "YES"
        else:
            print "NO"
        sock.close()
    sock.close()
