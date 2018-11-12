import socket
from _thread import *
host = '127.0.0.1'
port = 5600
def clientthread(conn):
     ch = conn.recv(1024).decode()
     if ch[0] == '3' :
         tcp_file_transfer()
     if ch[0] == '1' :
        tcp_chat()
     elif ch[0] == '2' :
        tcp_calculator()
def tcp_file_transfer():
    f = open('tcpftp.txt','rb')
    print('sending file ...')
    l = f.read(4096)
    while (l):
        print('sending...')
        conn.sendall(l)
        print(l)
        l = f.read(4096)
    f.close()
    print('file sent!')
    conn.shutdown(socket.SHUT_WR)
    conn.close()
def tcp_chat():
    while True:
        data = conn.recv(1024)
        print(addr,' says', data.decode())
        msg_to_client = input('enter message :')
        conn.sendall(msg_to_client.encode())
def tcp_calculator():
    while True:
        data = conn.recv(1024).decode()
        print(data)
        if data[1] == '+':
            res = int(data[0]) + int(data[2])
        if data[1] == '-':
            res = int(data[0]) - int(data[2])
        if data[1] == '/':
            res = int(data[0]) / int(data[2])
        if data[1] == '*':
            res = int(data[0]) * int(data[2])
        print(res)
        conn.send(str(res).encode())
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(10)
print('listening...')
while True:
    conn, addr = s.accept()
    print('user ',addr, ' connected ! ')
    start_new_thread(clientthread,(conn,))
