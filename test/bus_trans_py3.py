import socket
import threading
import time


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_host = input('server host: ')
port1 = input('server port: ')
server_port = int(port1)

client_host = input('client host: ')
port2 = input('client port: ')
client_port = int(port2)

#server.bind(('192.168.4.100', 8888))
server.bind((server_host, server_port))
server.listen(5)
print(server.getsockname())
print('waiting for connect...')
connect, (host, port) = server.accept()

peer_name = connect.getpeername()
sock_name = connect.getsockname()
print(u'the client %s:%s has connected.' % (host, port))
print('The peer name is %s and sock name is %s' % (peer_name, sock_name))

#client.connect(('192.168.4.102', 8886))
client.connect((client_host, client_port))

class Message:
           
    def listen(self):
        while True:
            Rx = connect.recv(1024)
            # hex_bytes = bytes.fromhex(data)
            hex_string = Rx.hex()
            #print(type(hex_string))
            
            #connect.sendall(b'your words has received.')
            print('the client say:' + hex_string )
            time.sleep(0.1)
            print('enter message:')
            # print(hex_string)
            # print(data)
    
    def talk(self):
        while True:
            print('enter message: ')
            Tx = input()
            

            if Tx == 'esc':
                #server.close()
                #client.close()
                print('bye！')
                # the feature undone
            else:
                try:
                    hex_data = bytes.fromhex(Tx)
                    client.sendall(hex_data)
                except:
                    print('transfrom hex fail')

            #data = data.encode('utf-8')
            
               
            
            #rec_data = client.recv(1024)
            #hex_string = rec_data.hex()
            #print('form server receive:' + hex_string)
    

if __name__ =='__main__':
    message=Message()
    #threads = []
       
    thread_listen=threading.Thread(target = message.listen, args = (),name='Listen')
    thread_talk=threading.Thread(target = message.talk, args = (),name='Talk')  

    thread_listen.start()
    thread_talk.start()

    thread_listen.join()
    thread_talk.join()   


server.close()
client.close()