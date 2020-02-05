import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = IPv4 , socket.SOCK_STREAM = socket(TCP) , DGRAM = socket(UDP)

client.connect(('192.168.4.102', 8886))
# connection address(host,port)

while True:

    data = input('enter message: ')
    #輸入 要傳輸的資料
    hex_data = bytes.fromhex(data)

    #data = data.encode('utf-8')
    #將字串編碼為byte

    client.sendall(hex_data)
    #傳輸資料

    #rec_data = client.recv(1024)
    #hex_string = rec_data.hex()
    #print('form server receive:' + hex_string)

client.close()
