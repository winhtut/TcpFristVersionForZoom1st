import socket
import threading

class TCPserver():
    def __init__(self,ip,port):
        self.server_ip=ip
        self.server_port=port
    def Server(self):
        #creating server
        server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        server.bind((self.server_ip,self.server_port))
        #start listening from server
        server.listen(5)
        print(f'Server is liestening on {self.server_ip} : {self.server_port}')

        while True:
            #connection accept
            client , address =server.accept()
            print(f'Accepted connection from {address}:')

            #transmit data and recive
            client_handler= threading.Thread(target=self.handle_client,args=(client,))
            client_handler.start()
    def handle_client(self,client_socket):
        with client_socket as sock:
            receive_data=sock.recv(1024)
            print(f'Server Received:{receive_data.decode("utf-8")}')
            html=open('index.html').read()

            tosend = ('HTTP/1.0 200 OK\n\n '+html).encode()


            sock.send(tosend)

if __name__=="__main__":
    server_ip='localhost'
    server_port=9999

    tcpServer=TCPserver(server_ip,server_port)
    tcpServer.Server()
