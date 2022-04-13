import socket
address = ('127.0.0.1', 10001)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(address)
s.listen(5)

while True:
    conn, address_client = s.accept()
    print('connected by ' + str(address_client))
    for i in range(5):
        data = b'Hello %d' % (i + 1)
        conn.send(data)
        recv_data = conn.recv(2048)
        print(recv_data)

    conn.close()
