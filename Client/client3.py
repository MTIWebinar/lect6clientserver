import socket

import sys

HOST, PORT = '78.47.201.69', 4001
data = ' '.join(sys.argv[1:])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    sock.sendall((data + '\n').encode('utf-8'))

    received = sock.recv(1024)
finally:
    sock.close()

print('Sent: {}'.format(data))
print('Received: {}'.format(received.decode('utf-8')))