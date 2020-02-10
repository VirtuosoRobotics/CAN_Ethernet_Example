import socket
import threading
import time

class CanEthernet:

    def __init__(self,server_ip,server_port,client_ip,client_port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((server_ip, server_port))
        self.server.listen(5)
        self.client.connect((client_ip, client_port))
        self.running = True
        self.rec_msg = ''
        print self.server.getsockname()
        print 'waiting for connect...'
        
    def server_listen(self):
        connect, (host, port) = self.server.accept()
        peer_name = connect.getpeername()
        sock_name = connect.getsockname()
        print 'the client %s:%s has connected.' % (host, port)
        print 'The peer name is %s and sock name is %s' % (peer_name, sock_name)
        while self.running:
            Rx = connect.recv(1024)
            hex_string = Rx.encode('hex')
            self.rec_msg = hex_string
            print 'the client say:' + hex_string 
            time.sleep(0.1)

    def client_send(self,input_msg): 
        try:  
            hex_data = input_msg.decode('hex')
            self.client.sendall(hex_data)
        except Exception as e:
            print e
            print('transfrom hex fail')

    def get_rcv_msg(self):
        return self.rec_msg

    def start_listen_talk(self):
        thread_listen=threading.Thread(target = self.server_listen, args = (),name='Listen')
        thread_listen.setDaemon(True)
        thread_listen.start()

    def end_listen(self):
        self.running = False
        


if __name__ =='__main__':
    can_bus = CanEthernet('192.168.4.100',8887,'192.168.4.101',8885)
    can_bus.start_listen_talk()

    while True:
        print('enter message: ')
        input_msg = raw_input()
        can_bus.client_send(input_msg)
        # print 'Receive data of 20 seconds ago: ' + can_bus.get_rcv_msg()
        # time.sleep(20)

    print 'stop'

