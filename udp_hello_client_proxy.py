import socket
address = ('127.0.0.1', 5406)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(50):
    data = b'Hello %d' % (i+1)
    s.sendto(data, address)
    recv_data, address_server = s.recvfrom(2048)
    print(recv_data)
