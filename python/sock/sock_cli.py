#!/usr/bin/env python

import subprocess
import socket

def sock_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 10000))
    while True:
        data = input('<--')
        if not data:
            break
        sock.send(data)
        print('sender info: %s' % data)
        if data.upper() == "EXIT":
            break
        rdata = sock.recv(512)
        if not rdata:
            break
        print('rece info --> ' + rdata)
    #sock.close()

def main():
    print "="*15 + "i am client" + "="*15
    sock_client()

if __name__ == '__main__':
    main()
