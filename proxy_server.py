#!/usr/bin/env python3
import socket
import time

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        sgoog = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sgoog.connect(('www.google.com', 80))
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            #recieve data, wait a bit, then send it back
            full_data = conn.recv(BUFFER_SIZE)
            print(full_data)
            time.sleep(0.5)
            request = full_data
            
            #sgoog.send(request.encode())

            try:
                sgoog.sendall(request)
                #sgoog.sendall(request.encode())
                conn.sendall(sgoog.recv(BUFFER_SIZE))
            except socket.error:
                print ('Send failed')
                sys.exit()
            #print("Payload sent successfully")

            #conn.sendall(sgoog.recv(BUFFER_SIZE))
            #conn.sendall(full_data)
            conn.close()

if __name__ == "__main__":
    main()
