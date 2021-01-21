#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        #sgoog = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #addr1 = socket.gethostbyname('www.google.com')
        #sgoog.connect((addr1, 80))
        #print (f'Socket Connected to {} on ip ')
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(1)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sgoog:
                addr1 = socket.gethostbyname('www.google.com')
                sgoog.connect((addr1, 80))
                #conn, addr = s.accept()
                #conn.sendall("hello".encode())
                p = Process(target=handle_echo, args = (addr,conn,sgoog))
                p.daemon = True
                p.start()
                print("Started process ",p)
            conn.close()


def handle_echo(addr, conn,sgoog):
    #conn.send("hello".encode())
    
    full_data = conn.recv(BUFFER_SIZE)
    #print(full_data)
    #time.sleep(0.5)
    request = full_data
    
    #sgoog.send(request.encode())

    try:
        sgoog.sendall(request)
        sgoog.shutdown(socket.SHUT_WR)
        #sgoog.sendall(request.encode())
        rec1 = sgoog.recv(BUFFER_SIZE)
        #print(rec1)
        conn.send(rec1)

    except socket.error:
        print ('Send failed')
        sys.exit()
    #print("Payload sent successfully")

    #conn.sendall(sgoog.recv(BUFFER_SIZE))
    #conn.sendall(full_data)
    

if __name__ == "__main__":
    main()
