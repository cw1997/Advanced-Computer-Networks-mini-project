import socket
address = ('127.0.0.1', 10001)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

for i in range(5):
    data = b'Hello %d' % (i+1)
    s.send(data)
    recv_data = s.recv(2048)
    print(recv_data)

s.close()
