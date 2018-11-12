import socket
import sys
import os
host = '127.0.0.1'
port = 5600
def tcp_file_transfer():
    f = open('tcpftp1.txt','wb')
    l = s.recv(4096)
    while (l):
        print('recieving file ...')
        f.write(l)
        l = s.recv(4096)
        print('...')
    f.close()
    print('file recieved !')
def tcp_chat():
    while True:
        inputStream = input("enter string :").encode()
        s.sendall(inputStream)
        data = s.recv(1024)
        print('message from ',data.decode())
def tcp_calculator():
    while True:
        input_info = input('enter number 1 number 2 and the operator: ')
        s.send(str(input_info).encode())
        data = s.recv(1024).decode()
        print(data)
ch = input('enter your choice :\n \t 1.chat\n \t 2.calculator\n \t 3.file transfer \t')
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host,port))
    s.send(ch.encode())
    if ch[0] == '1':
        tcp_chat()
    if ch[0] == '2':
        tcp_calculator()
    if ch[0] == '3' :
        tcp_file_transfer()
