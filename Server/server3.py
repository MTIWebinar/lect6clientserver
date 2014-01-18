#!/usr/bin/python

try:
    import SocketServer as socketserver
except ImportError:
    import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        decoded = self.data.decode('utf-8')
        print(decoded)
        self.request.sendall(decoded.upper().encode('utf-8'))


if __name__ == '__main__':
    HOST, PORT = '0.0.0.0', 4001
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()