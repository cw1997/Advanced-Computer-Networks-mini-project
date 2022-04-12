import socket
address = ('127.0.0.1', 10001)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

while True:
	data, address_client = s.recvfrom(2048)
	# if data == b'Hello':
	print(data)
	s.sendto(b'World', address_client)
