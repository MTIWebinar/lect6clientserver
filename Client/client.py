# -*- coding:utf-8 -*-

"""
Задание:
1. один создал сервака с некой логикой
2. другие подрубиться к нему и определяют, что сервак с данными делает
3. записать в файл in:out

"""

import socket

import sys

# HOST, PORT = '78.47.201.69', 4001
HOST, PORT = '127.0.0.1', 4001

data = ' '.join(sys.argv[1:]) # первый агрумент - это путь

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    sock.sendall((data + '\n').encode('utf-8'))

    received = sock.recv(1024)
finally:
    sock.close()

print('Sent: {}'.format(data))
print('Received: {}'.format(received.decode('utf-8')))

# писать в файл то, что пришло с сервака