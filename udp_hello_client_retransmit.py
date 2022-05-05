import socket

sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_recv.bind(('127.0.0.1', 5407))
sock_recv.settimeout(1)

for i in range(100):
    data = b'Hello %d' % (i + 1)
    sock_send.sendto(data, ('127.0.0.1', 5406))
    while True:
        try:
            data, address_server = sock_recv.recvfrom(32768)
            print(address_server, data)
            break
        except socket.timeout:
            sock_send.sendto(data, ('127.0.0.1', 5406))
