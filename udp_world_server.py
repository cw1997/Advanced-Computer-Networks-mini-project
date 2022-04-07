import socket
addr = ('127.0.0.1',10001)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(addr)

while True:
	data, addr_client = s.recvfrom(2048)
	# if data == b'Hello':
	print(data)
	s.sendto(b'World', addr_client)
