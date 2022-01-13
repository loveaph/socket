from http import client
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('192.168.1.3',8080))
while True:
    data = input('输入给服务器的信息：')
    client.send(data.encode('utf-8'))
    back_info = client.recv(1024).decode('utf-8')
    print(back_info)