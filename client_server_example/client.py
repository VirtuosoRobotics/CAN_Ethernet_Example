import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = IPv4 , socket.SOCK_STREAM = socket(TCP) , DGRAM = socket(UDP)

client.connect(('192.168.4.100', 8888))
# connection address(host,port)

data = input()
#輸入 要傳輸的資料

data = data.encode('utf-8')
#將字串編碼為byte

client.sendall(data)
#傳輸資料

rec_data = client.recv(1024)
print(b'form server receive:' + rec_data)

client.close()
