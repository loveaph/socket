from http import server
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('192.168.1.3',8080))
server.listen(5)
info,addr = server.accept()
while True:
    data = info.recv(1024)
    print('收到客户端信息：'+data.decode('utf-8'))
    send_data = input('返回数据：')
    info.send(send_data.encode('utf-8'))