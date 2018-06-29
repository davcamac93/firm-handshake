import socket
import time

print("David Camacho\n1000849812\nClient")

#establish IP, port number, and buffer size
TCP_IP = 'localhost'
TCP_PORT = 8080
BUFFER_SIZE = 1024

#create socket and connect to specified ip and port number
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#once it's open do the following
with open('received_file', 'wb') as f:
    print 'file opened'
    while True:
        #print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        print('data=%s', (data))
        if not data:
            f.close()
            print 'file close()'
            break
        # write data to a file
        f.write(data)

print('Successfully got the file')
s.close()
print('connection closed')
