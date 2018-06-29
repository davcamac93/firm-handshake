import socket
import time
from threading import Thread
from SocketServer import ThreadingMixIn

print("David Camacho\n1000849812\nServer")


#establish IP, port number, and buffer size
TCP_IP = 'localhost'
TCP_PORT = 8080
BUFFER_SIZE = 1024

#define multi threading
class ClientThread(Thread):
    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print " New thread started for "+ip+":"+str(port)

    def run(self):
        #declare text file to look for and open it
        filename='testing.txt'
        f = open(filename,'rb')
        #send while data in file
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                #print('Sent ',repr(l))
                l = f.read(BUFFER_SIZE)
            #if no file
            if not l:
                f.close()
                self.sock.close()
                break
# RTT
start_time = time.time()

#set socket
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

#make socket listen for a handshake and establish the connection
while True:
    tcpsock.listen(5)
    print "Waiting for incoming connections..."
    (conn, (ip,port)) = tcpsock.accept()
    print 'Got connection from ', (ip,port)
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)
    print("RTT: %s seconds" % (time.time() - start_time))

for t in threads:
    t.join()
