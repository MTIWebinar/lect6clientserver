#!/usr/bin/python
# -*- coding:utf-8 -*-

try:
    SocketServer as socketserver
except ImportError:
    import socketserver

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        decoded = self.data.decode('utf-8')
        print(self.data)
        self.request.sendall(decoded.upper().encode('utf-8'))
        # self.request.sendall(len(self.data))


if __name__ == '__main__':
    HOST, PORT = '0.0.0.0', 4001
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()