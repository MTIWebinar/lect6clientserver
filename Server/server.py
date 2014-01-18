#!/usr/bin/python

import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())
        # self.request.sendall(len(self.data))


if __name__ == '__main__':
    HOST, PORT = '0.0.0.0', 4001
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()